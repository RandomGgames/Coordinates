#Stores self's coordinates into scoreboards
execute store result score @s RAN.CoordX run data get entity @s Pos.[0]
execute store result score @s RAN.CoordY run data get entity @s Pos.[1]
execute store result score @s RAN.CoordZ run data get entity @s Pos.[2]
