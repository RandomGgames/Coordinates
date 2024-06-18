#1-98 RESERVED FOR MAIN MENU
#main menu
execute if score @s Coordinates matches 1 run function coordinates:menus/main
execute if score @s Coordinates matches 1 run scoreboard players set @s Coordinates 0
#power menu
execute if score @s Coordinates matches 2 run function coordinates:menus/power
execute if score @s Coordinates matches 2 run scoreboard players set @s Coordinates 0
#mode menu
execute if score @s Coordinates matches 3 run function coordinates:menus/modes
execute if score @s Coordinates matches 3 run scoreboard players set @s Coordinates 0
#color menu
execute if score @s Coordinates matches 4 run function coordinates:menus/color
execute if score @s Coordinates matches 4 run scoreboard players set @s Coordinates 0

#101-198 RESERVED FOR POWER MENU
#off
execute if score @s Coordinates matches 101 run scoreboard players set @s RAN.CoordPower 0
execute if score @s Coordinates matches 101 run scoreboard players set @s Coordinates 2
#always on
execute if score @s Coordinates matches 102 run scoreboard players set @s RAN.CoordPower 1
execute if score @s Coordinates matches 102 run scoreboard players set @s Coordinates 2
#map
execute if score @s Coordinates matches 103 run scoreboard players set @s RAN.CoordPower 2
execute if score @s Coordinates matches 103 run scoreboard players set @s Coordinates 2
#compass
execute if score @s Coordinates matches 104 run scoreboard players set @s RAN.CoordPower 3
execute if score @s Coordinates matches 104 run scoreboard players set @s Coordinates 2
#map/compass
execute if score @s Coordinates matches 105 run scoreboard players set @s RAN.CoordPower 4
execute if score @s Coordinates matches 105 run scoreboard players set @s Coordinates 2
#back
execute if score @s Coordinates matches 199 run scoreboard players set @s Coordinates 1

#201-298 RESERVED FOR MODES MENU
#1
execute if score @s Coordinates matches 201 run scoreboard players set @s RAN.CoordMode 0
execute if score @s Coordinates matches 201 run scoreboard players set @s Coordinates 3
#2
execute if score @s Coordinates matches 202 run scoreboard players set @s RAN.CoordMode 1
execute if score @s Coordinates matches 202 run scoreboard players set @s Coordinates 3
#3
execute if score @s Coordinates matches 203 run scoreboard players set @s RAN.CoordMode 2
execute if score @s Coordinates matches 203 run scoreboard players set @s Coordinates 3
#4
execute if score @s Coordinates matches 204 run scoreboard players set @s RAN.CoordMode 3
execute if score @s Coordinates matches 204 run scoreboard players set @s Coordinates 3
#5
execute if score @s Coordinates matches 205 run scoreboard players set @s RAN.CoordMode 4
execute if score @s Coordinates matches 205 run scoreboard players set @s Coordinates 3
#6
execute if score @s Coordinates matches 206 run scoreboard players set @s RAN.CoordMode 5
execute if score @s Coordinates matches 206 run scoreboard players set @s Coordinates 3
#back
execute if score @s Coordinates matches 299 run scoreboard players set @s Coordinates 1

#301-398 RESERVED FOR COLOR MENU
#white
execute if score @s Coordinates matches 301 run scoreboard players set @s RAN.CoordColor 0
execute if score @s Coordinates matches 301 run scoreboard players set @s Coordinates 4
#gray
execute if score @s Coordinates matches 302 run scoreboard players set @s RAN.CoordColor 1
execute if score @s Coordinates matches 302 run scoreboard players set @s Coordinates 4
#dark_gray
execute if score @s Coordinates matches 303 run scoreboard players set @s RAN.CoordColor 2
execute if score @s Coordinates matches 303 run scoreboard players set @s Coordinates 4
#black
execute if score @s Coordinates matches 304 run scoreboard players set @s RAN.CoordColor 3
execute if score @s Coordinates matches 304 run scoreboard players set @s Coordinates 4
#aqua
execute if score @s Coordinates matches 305 run scoreboard players set @s RAN.CoordColor 4
execute if score @s Coordinates matches 305 run scoreboard players set @s Coordinates 4
#dark_aqua
execute if score @s Coordinates matches 306 run scoreboard players set @s RAN.CoordColor 5
execute if score @s Coordinates matches 306 run scoreboard players set @s Coordinates 4
#blue
execute if score @s Coordinates matches 307 run scoreboard players set @s RAN.CoordColor 6
execute if score @s Coordinates matches 307 run scoreboard players set @s Coordinates 4
#dark_blue
execute if score @s Coordinates matches 308 run scoreboard players set @s RAN.CoordColor 7
execute if score @s Coordinates matches 308 run scoreboard players set @s Coordinates 4
#green
execute if score @s Coordinates matches 309 run scoreboard players set @s RAN.CoordColor 8
execute if score @s Coordinates matches 309 run scoreboard players set @s Coordinates 4
#dark_green
execute if score @s Coordinates matches 310 run scoreboard players set @s RAN.CoordColor 9
execute if score @s Coordinates matches 310 run scoreboard players set @s Coordinates 4
#yellow
execute if score @s Coordinates matches 311 run scoreboard players set @s RAN.CoordColor 10
execute if score @s Coordinates matches 311 run scoreboard players set @s Coordinates 4
#gold
execute if score @s Coordinates matches 312 run scoreboard players set @s RAN.CoordColor 11
execute if score @s Coordinates matches 312 run scoreboard players set @s Coordinates 4
#red
execute if score @s Coordinates matches 313 run scoreboard players set @s RAN.CoordColor 12
execute if score @s Coordinates matches 313 run scoreboard players set @s Coordinates 4
#dark_red
execute if score @s Coordinates matches 314 run scoreboard players set @s RAN.CoordColor 13
execute if score @s Coordinates matches 314 run scoreboard players set @s Coordinates 4
#light_purple
execute if score @s Coordinates matches 315 run scoreboard players set @s RAN.CoordColor 14
execute if score @s Coordinates matches 315 run scoreboard players set @s Coordinates 4
#dark_purple
execute if score @s Coordinates matches 316 run scoreboard players set @s RAN.CoordColor 15
execute if score @s Coordinates matches 316 run scoreboard players set @s Coordinates 4
#back
execute if score @s Coordinates matches 399 run scoreboard players set @s Coordinates 1
