import random
import os
from utils import *


def new_day():
    global current_day
    #were choosing a number been 5 and 20 and taking it away from hunger and thirst
    player["hunger"] -= random.randint(5,19)
    player["thirst"] -= random.randint(5,19)
    player["stamina"] += random.randint(30,49)
    
    #not allowing hunger and thirst to go below 0
    player["hunger"] = max(0, player["hunger"])
    player["thirst"] = max(0, player["thirst"])
    player["stamina"] = min(100, player["stamina"])

    #adding a day to the current day
    current_day += 1

    if player["hunger"] <= 0 or player["thirst"] <= 0 or player["health"] <= 0:
        print("You died!")
        exit()
    return player, current_day

def eating_food(current_food):
    if current_food is None:
        current_food = input("What food would you like to eat? ")
    
    if current_food in food:
        player["hunger"] += food[current_food]
        if player["hunger"] > 50:
            player["hunger"] = 50  # maximum hunger allowed is 50
        print(f"You ate {current_food}. Hunger is now {player['hunger']}")
    else:
        print(f"{current_food} is not available.")
    
    return player

def drink(current_liquid):
    if current_liquid in liquid:  
        player["thirst"] += liquid[current_liquid] 
        if player["thirst"] > 50: 
            player["thirst"] = 50 # maximum hunger allowed is 50
        print(f"You drank {current_liquid}. Thirst is now {player['thirst']}")
    else:
        print(f"{current_liquid} is not available.")
    return player

def day_options():
    #at the start of a new day were returning all needed stats so the play can always see them
    print("--- Player Stats ---")
    print("  Health:", player["health"])
    print("  Stamina:", player["stamina"])
    print("  Hunger:", player["hunger"])
    print("  Thirst:", player["thirst"])


    print(f"\n--- Day {current_day} ---")
    print ("1. Eat")
    print ("2. Drink")
    print ("3. End the day")
    print ("4. Show inventory")
    print ("5. Hunt food")
    print ("6. Gather water")
    print ("7. Gather materials")
    decision = input("What would you like to do today?\n")
    decision = decision.lower()

    if decision == "eat" or decision == "1":
        current_food = input ("what food would you like to eat?")
        eating_food(current_food)
    elif decision == "drink" or decision == "2":
        drink("water")
    elif decision == "End the day" or decision == "3":
        os.system('cls')
        new_day()
    elif decision == "show inventory" or decision == "4":
        show_inventory()
    elif decision == "hunt food" or decision == "5":
        animal_to_hunt = input ("what anaimal are you hunting?")
        hunt(animal_to_hunt)
    elif decision == "gather water" or decision == "6":
        gather_water()
    elif decision == "gather" or decision == "7":
        material = input ("what are you gathering?")
        gather(material)
    
def hunt(animal_name):
    animal = animals[animal_name]
    item_to_give = animal["item_to_give"]
    success_chance = animal["chance_to_succeed"]
    item_gain = animal["item_gain"]
    stamina_cost = animal["stamina_cost"]
    #danger isnt currently being used just a quick draft
    danger = animal["danger"]

    roll_chance = random.randint(0, 100)

    if roll_chance <= success_chance:
        if item_to_give in player_inventory:
            player_inventory[item_to_give] += item_gain
            print("You've gained", item_gain, item_to_give, "it cost", stamina_cost, "stamina")
        else:
            player_inventory[item_to_give] = item_gain
            print("You've gained", item_gain, item_to_give, "it cost", stamina_cost, "stamina")
    return
    
def gather(material):
    chance = 50
    double_item_chance = random.randint(0,100)
    default_item_gain = 1
    #0 is just a place holder
    stamina_cost = 0
    #this is the chance of getting x2 loot for being lucky, still a placeholder
    double_loot = 0

    if material in materials:
        mat = materials[material]
        stamina_cost = mat["stamina_cost"]
        double_loot = mat["double_chance"]
        if double_item_chance <= double_loot:
            default_item_gain *= 2
            print ("You got lucky and gathered double the items!")
        
        if material in player_inventory:
            player_inventory[material] += default_item_gain
            print("You've gained", default_item_gain, material, "it cost", stamina_cost, "stamina")
        else:
            player_inventory[material] = default_item_gain
            print("You've gained", default_item_gain, material, "it cost", stamina_cost, "stamina")
    
def gather_water():
    stamina_lost = 10
    player["stamina"] -=  stamina_lost
    print (f"stamina reduced by {stamina_lost} current stamina is" ,player["stamina"])
    if "water" in player_inventory:
        player_inventory["water"] += 1
        print ("We gathered 1 water")
    else:
        player_inventory["water"] = 1
        print ("We gathered 1 water")

def show_inventory():
    print("\n--- Inventory ---")
    if not player_inventory:
        print("Your inventory is empty.")
    else:
        for item, amount in player_inventory.items():
            print(f"{item}: {amount}")


for day in range(1, total_days + 1):
    
    day_over = False
    
    while not day_over:
        day_options()
    new_day()