import json
import logging
import logging.handlers
import os
import socket
import sys
import tempfile
import typing
import zipfile
from dataclasses import dataclass, field
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

logger = logging.getLogger(__name__)

__version__ = "0.0.0"  # Major.Minor.Patch

log_buffer = logging.handlers.MemoryHandler(
    capacity=0,
    flushLevel=logging.CRITICAL,
    target=None,
)

logger.addHandler(log_buffer)
logger.setLevel(logging.DEBUG)


@dataclass
class ScriptSettings:
    pack_name = "Load-Breaking"
    pack_version = "1.1.7"
    game_versions = "26.1-26.1.2"
    files_to_zip = [
        Path(r"assets"),
        Path(r"data"),
        Path(r"pack.mcmeta"),
        Path(r"pack.png"),
    ]


@dataclass
class LogSettings:
    mode: typing.Literal["per_run", "latest", "per_day", "single_file", "console_only"] = "latest"
    folder: Path = Path("")
    console_level: int = logging.DEBUG
    file_level: int = logging.DEBUG
    date_format: str = "%Y-%m-%dT%H:%M:%S"
    message_format: str = "%(asctime)s.%(msecs)03d [%(levelname)-8s] %(message)s"
    # message_format: str = "%(asctime)s.%(msecs)03d [%(levelname)-8s] %(module)s:%(funcName)s - %(message)s"
    max_files: int | None = 30
    open_log_after_run: bool = False


@dataclass
class RuntimeSettings:
    pause_on_error: bool = True
    always_pause: bool = False


@dataclass
class Config:
    script_settings: ScriptSettings = field(default_factory=ScriptSettings)
    log_settings: LogSettings = field(default_factory=LogSettings)
    runtime_settings: RuntimeSettings = field(default_factory=RuntimeSettings)


def zip_files(files: list[Path], zip_path: Path, compresslevel: int = 6, error_on_missing: bool = False, overwrite: bool = True) -> None:
    """
    Create a zip archive from a list of Path objects safely using a temporary file.

    Accepts paths to files or directories. Directories are added recursively, 
    preserving their internal structures under their top-level folder name.
    """
    zip_path = Path(zip_path)

    if zip_path.exists() and not overwrite:
        raise FileExistsError(f"The destination file already exists and overwrite is disabled: {zip_path}")

    zip_path.parent.mkdir(parents=True, exist_ok=True)

    temp_file = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=zip_path.parent,
            prefix=f"{zip_path.name}.tmp_",
            delete=False
        ) as tmp_f:
            temp_file = Path(tmp_f.name)

            with zipfile.ZipFile(tmp_f, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=compresslevel) as zipf:
                for src_path in files:
                    src_path = Path(src_path)

                    if not src_path.exists():
                        if error_on_missing:
                            raise FileNotFoundError(f"Source path missing: {src_path}")
                        continue

                    if src_path.is_dir():
                        base_folder_name = src_path.name

                        for item in src_path.rglob("*"):
                            if item.is_file():
                                # Reconstruct the path relative to the parent of the target directory
                                relative_path = item.relative_to(src_path)
                                item_arcname = Path(base_folder_name) / relative_path
                                zipf.write(item, arcname=str(item_arcname))

                    else:
                        zipf.write(src_path, arcname=src_path.name)

        os.replace(temp_file, zip_path)
        logger.info("Successfully created archive: %s", zip_path)

    except Exception:
        if temp_file and temp_file.exists():
            try:
                temp_file.unlink()
            except OSError:
                pass
        logger.exception("Failed to create zip archive %s", zip_path)
        raise


def main(config: Config):
    pack_name = config.script_settings.pack_name
    files_to_zip = config.script_settings.files_to_zip
    pack_version = config.script_settings.pack_version
    game_versions = config.script_settings.game_versions

    file_name = Path(f"{pack_name}-{pack_version}.zip")

    release_title = Path(f"{pack_name} {pack_version} for {game_versions}")
    logger.debug("Release title: %s", release_title)

    zip_files(files=files_to_zip, zip_path=file_name)


def enforce_max_log_count(dir_path: Path, max_count: int, script_name: str) -> None:
    """
    Enforce a maximum number of log files for this script.

    Rules:
    - Only affects files ending with `.log`
    - Only affects logs that contain the script name
    - Sorting is performed lexicographically by filename
    """
    if max_count <= 0:
        return

    if not dir_path.exists():
        return

    log_files = [f for f in dir_path.glob("*.log") if script_name in f.name]
    if len(log_files) <= max_count:
        return
    log_files.sort(key=lambda p: p.name)
    to_delete = log_files[:-max_count]
    for file in to_delete:
        try:
            file.unlink()
            logger.debug("Removed old log %s", file)
        except OSError as e:
            logger.debug("Failed removing old log %s: %s", file, e)


def build_log_path(log_settings: LogSettings) -> Path | None:
    """
    Builds the final log file path based on logging mode.
    """
    if log_settings.mode == "console_only":
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    day_stamp = datetime.now().strftime("%Y%m%d")

    script_name = Path(__file__).stem

    log_dir = Path(log_settings.folder).expanduser().resolve()

    match log_settings.mode:
        case "per_run":
            filename = f"{timestamp}__{script_name}.log"
        case "latest":
            filename = f"{script_name}.log"
        case "per_day":
            filename = f"{day_stamp}__{script_name}.log"
        case "single_file":
            filename = f"{script_name}.log"
        case _:
            filename = f"{timestamp}__{script_name}.log"

    return log_dir / filename


class JsonArgsFilter(logging.Filter):
    """
    Automatically formats log arguments using JSON serialization rules.
    Guarantees double quotes around strings and paths without manual formatting.
    """

    def filter(self, record: logging.LogRecord) -> bool:
        if record.args:
            # Normalize arguments into a flat list for processing
            raw_args = list(record.args) if isinstance(record.args, tuple) else [record.args]
            processed_args: list[str] = []

            for val in raw_args:
                if isinstance(val, Path):
                    processed_args.append(json.dumps(val.as_posix(), default=str))
                elif isinstance(val, str):
                    processed_args.append(json.dumps(val))
                else:
                    processed_args.append(json.dumps(val, default=str))

            # Cast back to tuple so the logger can unpack it safely
            record.args = tuple(processed_args)
        return True


def setup_logging(logger_obj: logging.Logger, log_settings: LogSettings) -> Path | None:
    """
    Set up console and file logging.
    """
    logger_obj.handlers.clear()
    logger_obj.setLevel(logging.DEBUG)
    logger_obj.propagate = False

    # Attach the automatic JSON formatting filter
    logger_obj.addFilter(JsonArgsFilter())

    log_path = build_log_path(log_settings)

    formatter = logging.Formatter(
        log_settings.message_format,
        datefmt=log_settings.date_format,
    )

    if log_path:
        try:
            log_path.parent.mkdir(parents=True, exist_ok=True)

        except OSError as e:
            raise RuntimeError(f"Failed creating log directory {log_path.parent}") from e

        file_handler: logging.Handler

        match log_settings.mode:
            case "per_day":
                file_handler = TimedRotatingFileHandler(filename=log_path, when="midnight", interval=1, backupCount=log_settings.max_files or 0, encoding="utf-8")
            case "single_file":
                file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
            case _:
                file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")

        file_handler.setLevel(log_settings.file_level)
        file_handler.setFormatter(formatter)
        logger_obj.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_settings.console_level)
    console_handler.setFormatter(formatter)

    logger_obj.addHandler(console_handler)

    write_banner(logger_obj)

    if log_buffer:
        class _ForwardToLogger(logging.Handler):
            def emit(self, record):
                logger_obj.handle(record)

        forward_handler = _ForwardToLogger()
        log_buffer.setTarget(forward_handler)
        log_buffer.flush()
        log_buffer.close()

    if (log_settings.max_files and log_path and log_settings.mode not in ("per_day", "console_only")):
        enforce_max_log_count(dir_path=log_path.parent, max_count=log_settings.max_files, script_name=Path(__file__).stem)

    return log_path


def write_banner(logger_obj: logging.Logger):
    """
    Writes a clean session banner without log prefixes.
    """
    separator = "-" * 80

    banner = (
        f"{separator}\n"
        f"SCRIPT     | {json.dumps(Path(__file__).resolve().as_posix())}\n"
        f"VERSION    | {__version__}\n"
        f"START TIME | {datetime.now().isoformat(timespec='milliseconds')}\n"
        f"USER       | {os.getlogin()}\n"
        f"HOST       | {socket.gethostname()}\n"
        f"RUNTIME    | Python {sys.version.split()[0]}\n"
        f"{separator}"
    )

    original_formatters = {}

    class RawFormatter(logging.Formatter):
        """
        Formatter that outputs only the log message with no prefixes.
        """

        def format(self, record):
            return record.getMessage()

    try:
        for handler in logger_obj.handlers:
            original_formatters[handler] = handler.formatter
            handler.setFormatter(RawFormatter())

        logger_obj.info(banner)

    finally:
        for handler, formatter in original_formatters.items():
            handler.setFormatter(formatter)


def bootstrap():
    exit_code = 0
    log_path: Path | None = None
    config = Config()

    try:
        log_path = setup_logging(logger_obj=logger, log_settings=config.log_settings)
        main(config)

    except KeyboardInterrupt:
        logger.warning("Operation interrupted by user.")
        exit_code = 130

    except Exception as e:
        logger.exception("A fatal error has occurred: %s", e)
        exit_code = 1

    if (config.log_settings.open_log_after_run and log_path and log_path.exists()):
        try:
            match sys.platform:
                case plat if plat.startswith("win"):
                    os.startfile(log_path)
                case "darwin":
                    os.system(f'open "{log_path}"')
                case _:
                    os.system(f'xdg-open "{log_path}"')

        except Exception as e:
            logger.warning("Failed to open log file: %s", e)

    if (config.runtime_settings.always_pause or (config.runtime_settings.pause_on_error and exit_code != 0)):
        input("Press Enter to exit...")

    return exit_code


if __name__ == "__main__":
    sys.exit(bootstrap())
