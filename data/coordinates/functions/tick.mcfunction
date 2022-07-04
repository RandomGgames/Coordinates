#Inform players about data pack and set default settings
scoreboard players add @a RAN.CoordNew 0
execute as @a if score @s RAN.CoordNew matches 0 run function coordinates:new

#Allows the trigger command to access the control panel and buttons
scoreboard players enable @a Coordinates
execute as @a if score @s Coordinates matches 1.. run function coordinates:trigger

#Show the coordinates display to the player depending on the power mode
execute as @a if score @s RAN.CoordPower matches 1 run function coordinates:modes/root
execute as @a if score @s RAN.CoordPower matches 2 if predicate coordinates:holding_map run function coordinates:modes/root
execute as @a if score @s RAN.CoordPower matches 3 if predicate coordinates:holding_compass run function coordinates:modes/root
execute as @a if score @s RAN.CoordPower matches 4 if predicate coordinates:holding_compass_or_map run function coordinates:modes/root
