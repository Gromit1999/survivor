#player stats
player = {
    "health": 100,
    "stamina": 100,
    "hunger": 50,
    "thirst": 50
}
#player inventory / starting inventory
player_inventory = {
    "Rabbit": 1,
    "axe": 1,
    "pickaxe": 1
}
#food stats
food = {
    "berries": 10,
    "fish": 25,
    "apple":5,
    "rabbit":28
}
#liquid stats
liquid = {
    "water": 20
}
#animals
rabbit = {
    "chance_to_succeed": 100,
    "item_gain": 1,
    "item_to_give": "Raw rabbit",
    "stamina_cost": 5,
    "danger": 0
}

deer = {
    "chance_to_succeed": 80,
    "item_gain": 1,
    "item_to_give": "Raw deer meat",
    "stamina_cost": 15,
    "danger": 10
}

boar = {
    "chance_to_succeed": 60,
    "item_gain": 1,
    "item_to_give": "Raw boar meat",
    "stamina_cost": 20,
    "danger": 25
}

wolf = {
    "chance_to_succeed": 50,
    "item_gain": 1,
    "item_to_give": "Raw wolf meat",
    "stamina_cost": 25,
    "danger": 35
}

bear = {
    "chance_to_succeed": 30,
    "item_gain": 1,
    "item_to_give": "Raw bear meat",
    "stamina_cost": 40,
    "danger": 50
}

fish = {
    "chance_to_succeed": 90,
    "item_gain": 1,
    "item_to_give": "Raw fish",
    "stamina_cost": 10,
    "danger": 0
}

animals = {
    "rabbit": rabbit,
    "deer": deer,
    "boar": boar,
    "wolf": wolf,
    "bear": bear,
    "fish": fish
}
#things we can start gathering we need a list of things to gather just putting wood here just as a placeholder for how i want to structure it
wood = {
    "item_gain": 1,
    "stamina_cost": 10,
    #kind of like a swift swing gives you 2 items instead of one, also using the approaite tool or having the apprioate tool will 
    #give you 2x, so it will be 2x2 which will give you 4 for the same stamina as gaining one normally
    "double_chance": 20,
    "bonus_tool": "axe"
}

iron = {
    "item_gain": 1,
    "stamina_cost": 10,
    #kind of like a swift swing gives you 2 items instead of one, also using the approaite tool or having the apprioate tool will 
    #give you 2x, so it will be 2x2 which will give you 4 for the same stamina as gaining one normally
    "double_chance": 20,
    "bonus_tool": "pickaxe"
}

materials = {
    "wood": wood,
    "iron": iron
}

total_days = 30
current_day = 0