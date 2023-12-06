import random
import math
from helper_functions.create_entity import make_pre_lv_10_field_mobs, make_post_lv_10_field_mobs
from helper_functions.display_for_users import print_board, slow_print


def determine_event(board, character, shop):
    """
    Determine what event is triggered based on the character's current position

    :param board: a dictionary with tuples as keys and strings as values
    :param character: a dictionary with strings as keys and values
    :param shop: a list of dictionaries
    :precondition board: a dictionary with tuples as keys and strings as values
    :precondition character: a dictionary with strings as keys and values
    :precondition shop: a list of dictionaries
    :postcondition: determines what event is triggered based on the character's current position
    :return: None

    """
    current_position = board[(character["x-position"], character["y-position"])]
    if current_position == '^' and chance_of_event(0.40):
        combat(character, make_pre_lv_10_field_mobs()[random.randint(0, 1)])
    elif current_position == '*' and chance_of_event(0.50):
        combat(character, make_post_lv_10_field_mobs()[random.randint(0, 1)])
    elif current_position == 'S':
        shop_event(character, shop)
    elif current_position == 'H':
        healing_altar(character)
    elif current_position == '/':
        check_if_lvl_10(character, board)
    elif current_position == 'T':
        treasure_event(character, board)


def chance_of_event(probability):
    """
    Determine if an event will occur based on the probability
    
    :param probability: a float
    :precondition probability: a float between 0 and 1
    :postcondition: determines if an event will occur based on the probability
    :return: a boolean

    """
    random_number = random.uniform(0, 1)

    if random_number <= probability:
        return True
    else:
        return False


def check_if_lvl_10(character, board):
    """
    Check if the character is level 10 or higher
    
    :param character: a dictionary
    :param board: a dictionary
    :precondition character: a dictionary with strings as keys and values
    :precondition board: a dictionary with tuples as keys and strings as values
    :postcondition: checks if the character is level 10 or higher

    """
    if character["level"] < 10:
        slow_print("\nGatekeeper: You shall not pass!!! The roads ahead are too dangerous for \na low "
              "level peasant like you. Come back when you hit level 10.\n"
              "You are pushed back roughly by the gatekeeper.\n")
        character["y-position"] += 1
        print_board(board, character)


def treasure_event(character, board):
    """
    Trigger a treasure event
    
    :param character: a dictionary
    :param board: a dictionary
    :precondition character: a dictionary with strings as keys and values
    :precondition board: a dictionary with tuples as keys and strings as values
    :postcondition: triggers a treasure event
    """
    mystery_potion = random.randint(1, 10)
    slow_print("\nCongratulations! You have found a treasure box!")
    slow_print("You open the chest to find a small vial with luscious purple liquid sloshing around.\n")
    user_input = input("Drink this liquid? Enter 'y' to drink, 'n' to throw away: \n").lower().strip()
    if user_input == 'y':
        if mystery_potion <= 3:
            slow_print("It was actually something good! Gain 10 maxHP!")
            character["maxHP"] += 10
            character["currentHP"] += 10
            slow_print(f"Your HP: {character['currentHP']} / {character['maxHP']}\n")
        elif mystery_potion > 3:
            slow_print("Why are you drinking random shit off the ground? You deserve this. Lose 10 maxHP.")
            character["maxHP"] -= 10
            character["currentHP"] -= 10
            slow_print(f"Your HP: {character['currentHP']} / {character['maxHP']}\n")
    # remove treasure event after event finishes
    board[(character["x-position"], character["y-position"])] = '^'


def check_exp(character):
    """
    Check if currentEXP is higher than or equal to maxEXP.

    If it is, change stats accordingly. Nothing happens otherwise.

    :param character: a dictionary
    """
    if character["currentEXP"] >= character["maxEXP"]:
        character["level"] += 1
        character["currentEXP"] = int(character["currentEXP"] - character["maxEXP"])
        character["maxEXP"] = int(character["maxEXP"] * 1.1)
        character["currentHP"] = int(character["currentHP"] * 1.1)
        character["maxHP"] = int(character["maxHP"] * 1.1)
        character["atk"] = int(math.ceil(character["atk"] * 1.1))
        slow_print(f"You have leveled up! You are now level {character['level']}. "
              f"You feel stronger, as the aura around you settles down.")
        slow_print(f"Your new stats --- HP: {character['currentHP']} / {character['maxHP']} --- "
              f"ATK: {character['atk']} --- EXP: {character['currentEXP']} / {character['maxEXP']}")


def healing_altar(character):
    """
    Heal the character to full HP
    
    :param character: a dictionary
    :precondition character: a dictionary with strings as keys and values
    :postcondition: heals the character to full HP
    """
    character["currentHP"] = character["maxHP"]
    slow_print("\nYou are at the healing altar. Heal yourself to full.\n"
          f"You now have {character['currentHP']} / {character['maxHP']} HP. \n")


def combat(character, enemy):
    """
    Trigger a combat event
    
    :param character: a dictionary
    :param enemy: a dictionary
    :precondition character: a dictionary with strings as keys and values
    :precondition enemy: a dictionary with strings as keys and values
    :postcondition: triggers a combat event
    """
    slow_print(f"\nYou have encountered a wild {enemy['name']}!!")
    while character["currentHP"] > 0 and enemy["currentHP"] > 0:
        slow_print(f"Current Status: ")
        slow_print(f"Your HP: {character['currentHP']} / {character['maxHP']}")
        slow_print(f"{enemy['name']}'s HP: {enemy['currentHP']} / {enemy['maxHP']}\n")
        user_choice = input('Enter "x" to attack or "z" to run away: ')
        if user_choice == 'x':
            user_roll = random.randint(1, 12)
            slow_print(f"You rolled the die of fate... to roll {user_roll}!\n")
            damage = character["atk"] * user_roll
            enemy["currentHP"] -= damage
            slow_print(f"You used {character['move']}!")
            slow_print(f"You dealt {damage} damage to {enemy['name']}!")
            slow_print(f"{enemy['name']}'s HP: {enemy['currentHP']} / {enemy['maxHP']}\n")
            if enemy["currentHP"] > 0:
                character["currentHP"] -= enemy["atk"]
                slow_print(f"{enemy['name']} attacked you for {enemy['atk']}.")
                slow_print(f"Your HP: {character['currentHP']} / {character['maxHP']}\n")
            else:
                character["gold"] += enemy["gold"]
                character["currentEXP"] += enemy["EXP"]
                slow_print(f"You earned {enemy['gold']} gold! You now have {character['gold']} gold.")
                slow_print(f"You earned {enemy['EXP']} XP! You now have "
                      f"{character['currentEXP']}/{character['maxEXP']} XP.\n\n")
                check_exp(character)
        elif user_choice == 'z':
            if enemy["runnable"]:
                slow_print("You run away, shrieking like a little girl. To think that the fate of "
                      "this world lies on the likes of you...\n")
                break
            else:
                slow_print(f"\n{enemy['name']}: You cannot run, you cannot hide... I AM INEVITABLE!!!")
                slow_print("You cannot run from a boss fight. Just die in battle.\n")


def shop_event(character, shop):
    """
    Trigger a shop event
    
    :param character: a dictionary
    :param shop: a list of dictionaries
    :precondition character: a dictionary with strings as keys and values
    :precondition shop: a list of dictionaries
    :postcondition: triggers a shop event
    """
    slow_print("Welcome, hero. I have travelled thousands of miles to be of assistance."
          "Here are the items that I have managed to bring for you."
          "But they aren't free. I still have to feed my family you know?\n")
    for index, item in enumerate(shop, start=1):
        slow_print(f"{index}. Item name: {item['name']}, Price: {item['price']} gold, {item['effect']}")

    slow_print(f"\nYou currently have {character['gold']} gold.\n")
    while True:
        user_input = input("Enter the number of the item you wish to buy, or 'q' to quit: ")
        if user_input == '1':
            if shop[0]["amount"] <= 0:
                slow_print("Sorry, you already bought out those items.")
            elif shop[0]["price"] > character["gold"]:
                slow_print("Come back with enough gold you swine!!! Nothing is free in my town!!!")
            else:
                character["gold"] -= shop[0]["price"]
                shop[0]["amount"] -= 1
                character["currentHP"] += shop[0]["added_HP"]
                character["maxHP"] += shop[0]["added_HP"]
                slow_print(f"You have purchased the {shop[0]['name']}.")
                slow_print(f"Your HP is now {character['currentHP']} / {character['maxHP']}.")
                slow_print(f"You now have {character['gold']} gold.")
        elif user_input == '2':
            if shop[1]["amount"] <= 0:
                slow_print("Sorry, you already bought out those items.")
            elif shop[1]["price"] > character["gold"]:
                slow_print("Come back with enough gold you swine!!! Nothing is free in my town!!!")
            else:
                character["gold"] -= shop[1]["price"]
                shop[1]["amount"] -= 1
                character["atk"] += shop[1]["added_ATK"]
                character["move"] = shop[1]["move_upgrade"]
                slow_print(f"You have purchased the {shop[1]['name']}.")
                slow_print(f"Your ATK is now {character['atk']}.")
                slow_print(f"You now attack with {character['move']}.")
                slow_print(f"You now have {character['gold']} gold.")
        elif user_input == '3':
            if shop[2]["amount"] <= 0:
                slow_print("Sorry, you already bought out those items.")
            elif shop[2]["price"] > character["gold"]:
                slow_print("Come back with enough gold you swine!!! Nothing is free in my town!!!")
            else:
                character["gold"] -= shop[2]["price"]
                shop[2]["amount"] -= 1
                character["currentEXP"] += shop[2]["added_EXP"]
                slow_print(f"You have purchased the {shop[2]['name']}.")
                check_exp(character)
                slow_print(f"Your ATK is now {character['atk']}.")
                slow_print(f"You now have {character['gold']} gold.")
        elif user_input == 'q':
            slow_print("Thank you for your patronage.")
            break
        else:
            slow_print("We don't sell anything like that... choose something else.")


def main():
    mob = {"name": "Legion Soldier", "currentHP": 300, "maxHP": 1000, "atk": 10, "EXP": 25, "gold": 5}
    character = {"name": "BoB", "maxHP": 100, "gold": 0, "level": 1,
                 "currentHP": 100, "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                 "x-position": 10, "y-position": 20, "model": "O"}
    slow_print(character)

    combat(character, mob)

    slow_print(character)


if __name__ == "__main__":
    main()
