#Get the coordinates of the player
execute as @s run function coordinates:modes/get_coordinates

#Call mode to display coordinates
execute as @s if score @s RAN.CoordMode matches 0 run function coordinates:modes/0/root
execute as @s if score @s RAN.CoordMode matches 1 run function coordinates:modes/1/root
execute as @s if score @s RAN.CoordMode matches 2 run function coordinates:modes/2/root
execute as @s if score @s RAN.CoordMode matches 3 run function coordinates:modes/3/root
execute as @s if score @s RAN.CoordMode matches 4 run function coordinates:modes/4/root
execute as @s if score @s RAN.CoordMode matches 5 run function coordinates:modes/5/root
