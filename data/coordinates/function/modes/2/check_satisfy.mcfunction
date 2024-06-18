execute if score @s RAN.CoordPower matches 1 run scoreboard players set @s RAN.CoordSatisfy 1
execute if score @s RAN.CoordPower matches 2 if data entity @s {SelectedItem:{id:"minecraft:filled_map"}} run scoreboard players set @s RAN.CoordSatisfy 1
execute if score @s RAN.CoordPower matches 2 if data entity @s {Inventory:[{id:"minecraft:filled_map",Slot:-106b}]} run scoreboard players set @s RAN.CoordSatisfy 1
execute if score @s RAN.CoordPower matches 3 if data entity @s {SelectedItem:{id:"minecraft:compass"}} run scoreboard players set @s RAN.CoordSatisfy 1
execute if score @s RAN.CoordPower matches 3 if data entity @s {Inventory:[{id:"minecraft:compass",Slot:-106b}]} run scoreboard players set @s RAN.CoordSatisfy 1
execute if score @s RAN.CoordPower matches 4 if data entity @s {SelectedItem:{id:"minecraft:filled_map"}} run scoreboard players set @s RAN.CoordSatisfy 1
execute if score @s RAN.CoordPower matches 4 if data entity @s {Inventory:[{id:"minecraft:filled_map",Slot:-106b}]} run scoreboard players set @s RAN.CoordSatisfy 1
execute if score @s RAN.CoordPower matches 4 if data entity @s {SelectedItem:{id:"minecraft:compass"}} run scoreboard players set @s RAN.CoordSatisfy 1
execute if score @s RAN.CoordPower matches 4 if data entity @s {Inventory:[{id:"minecraft:compass",Slot:-106b}]} run scoreboard players set @s RAN.CoordSatisfy 1

execute if score @s RAN.CoordSatisfy matches 1.. run function coordinates:modes/root
