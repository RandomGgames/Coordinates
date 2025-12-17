#Default settings for players
scoreboard players set @s RAN.CoordMode 0
scoreboard players set @s RAN.CoordColor 0
scoreboard players set @s RAN.CoordPower 1

#Inform player about datapack
tellraw @s ["",{"text":"RandomGgames' Coordinates Data Pack","color":"gold","bold":true},{"text":"\nTo use the data pack, run the command ","color":"aqua"},{"text":"\"/trigger Coordinates\"","color":"dark_aqua","click_event":{"action":"run_command","command":"/trigger Coordinates"}},{"text":" to access the control panel. There, you can turn off the coordinate display, change the color, and change the mode.","color":"aqua"}]

#Code stuff
scoreboard players set @s RAN.CoordNew 1
