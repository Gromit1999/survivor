import random
import os

#player stats
player = {
    "health": 100,
    "stamina": 100,
    "hunger": 50,
    "thirst": 50
}
#player inventory
player_inventory = {
    "rabbit": 1
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

#amount of total days to survive and current day were on
total_days = 30
current_day = 0


def new_day():
    global current_day
    #were choosing a number been 5 and 20 and taking it away from hunger and thirst
    player["hunger"] -= random.randint(5,20)
    player["thirst"] -= random.randint(5,20)
    
    #not allowing hunger and thirst to go below 0
    player["hunger"] = max(0, player["hunger"])
    player["thirst"] = max(0, player["thirst"])

    #adding a day to the current day
    current_day += 1

    if player["hunger"] <= 0 or player["thirst"] <= 0:
        print("You died!")
        exit()
    return player, current_day

def eating_food(current_food):
    if current_food in food:  
        player["hunger"] += food[current_food] 
        if player["hunger"] > 50: 
            player["hunger"] = 50 # maximum hunger allowed is 50
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
    print("Player Stats:")
    print("  Health:", player["health"])
    print("  Hunger:", player["hunger"])
    print("  Thirst:", player["thirst"])
    print("  Stamina:", player["stamina"])

    print(f"\n--- Day {current_day} ---")
    print ("1. Eat")
    print ("2. Drink")
    print ("3. Sleep")
    print ("4. Show inventory")
    print ("5. Hunt")
    decision = input("What would you like to do today?\n")

    if decision == "eat" or decision == "1":
        pass
    elif decision == "drink" or decision == "2":
        pass
    elif decision == "sleep" or decision == "3":
        os.system('cls')
        new_day()
    elif decision == "show inventory" or decision == "4":
        show_inventory()
    elif decision == "hunt" or decision == "5":
        hunt("rabbit", 1)
    
def hunt(item, amount= 1):
    if item in player_inventory:
        player_inventory[item] += amount
        print("we hunted and gained:5", amount, item)
    else:
        player_inventory[item] = amount

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