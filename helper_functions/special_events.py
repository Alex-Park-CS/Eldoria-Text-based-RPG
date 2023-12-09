import random
import math
from helper_functions.display_for_users import slow_print
from helper_functions.create_entity import (
    make_pre_lv_10_field_mobs,
    make_post_lv_10_field_mobs,
    make_marbas,
    make_andromalius
)


def determine_event(board, character, shop, boss) -> None:
    """
    Determine what event is triggered based on the character's current position

    :param board: a dictionary with tuples as keys and strings as values
    :param character: a dictionary with strings as keys and values
    :param shop: a list of dictionaries
    :param boss: a dictionary with strings as keys and values
    :precondition board: a dictionary with tuples as keys and strings as values
    :precondition character: a dictionary with strings as keys and values
    :precondition shop: a list of dictionaries
    :precondition boss: a dictionary of the final boss
    :postcondition: determines what event is triggered based on the character's current position and initiate event
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
        check_if_lvl_10(character)
    elif current_position == 'T':
        treasure_event(character, board)
    elif current_position == '-':
        check_for_orbs(character)
    elif current_position == 'A':
        combat_andromalius(character, make_andromalius())
    elif current_position == 'M':
        combat_marbas(character, make_marbas())
    elif current_position == 'B':
        combat_baal(character, boss)
        if boss["currentHP"] <= 0:
            slow_print(f"Baal: Arggh...AGGHHH...AHHHHHHHHHHHH!!! IT CAN'T BE!!! I WAS THE CHOSEN ONE!!! "
                       f"I WAS SUPPOSED TO BRING BALANCE TO THE WORLD!!! AAAAARRRRGGGGHHHHHH!!!!!!!!!!")
        else:
            slow_print(f"Although I waited for a blood-heating battle for eons... I assume this is the limits of "
                       f"your inferior race...Farewell, weakling.")


def chance_of_event(probability) -> bool:
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


def check_if_lvl_10(character) -> None:
    """
    Check if the character is level 10 or higher
    
    :param character: a dictionary
    :precondition character: a dictionary with strings as keys and values
    :postcondition: checks if the character is level 10 or higher

    >>> character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
    ...              "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
    ...              "x-position": 10, "y-position": 20, "orb": 0}
    
    >>> check_if_lvl_10(character_test)
    <BLANKLINE>
    Gatekeeper: You shall not pass!!! The roads ahead are too dangerous for
    a low level peasant like you. Come back when you hit level 10.
    You are pushed back roughly by the gatekeeper.
    <BLANKLINE>
    
    >>> character_test["level"] = 10
    >>> check_if_lvl_10(character_test)

    """
    if character["level"] < 10:
        slow_print("\nGatekeeper: You shall not pass!!! The roads ahead are too dangerous for\na low "
                   "level peasant like you. Come back when you hit level 10.\n"
                   "You are pushed back roughly by the gatekeeper.\n")
        character["y-position"] += 1


def check_for_orbs(character) -> None:
    """
    Check if the character has 2 orbs to pass the gates
    
    :param character: a dictionary
    :precondition character: a dictionary with strings as keys and values
    :postcondition: checks if the character has 2 orbs to pass the gates

    >>> character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
    ...              "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
    ...              "x-position": 10, "y-position": 20, "orb": 0}
    
    >>> check_for_orbs(character_test)
    <BLANKLINE>
    The two massive doors are sealed shut, and you see two divots in the shape of a sphere.
    You are pushed back roughly by an unknown force.
    <BLANKLINE>
    
    >>> character_test["orb"] = 2
    >>> check_for_orbs(character_test)
    The two orbs in your inventory fly out and fit right into the divots of the door.
    The door slowly creaks open, to uncover a long corridor...
    <BLANKLINE>
    """
    if character["orb"] < 2:
        slow_print("\nThe two massive doors are sealed shut, and you see two divots in the shape of a sphere.\n"
                   "You are pushed back roughly by an unknown force.\n")
        character["y-position"] += 1
    else:
        print("The two orbs in your inventory fly out and fit right into the divots of the door.\n"
              "The door slowly creaks open, to uncover a long corridor...\n")


def treasure_event(character, board) -> None:
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
    while True:
        user_input = input("Drink this liquid? Enter 'y' to drink, 'n' to throw away: \n").lower().strip()
        if user_input == 'y':
            if mystery_potion <= 6:
                slow_print("The purple liquid revitalizes you. Gain 10 maxHP!")
                character["maxHP"] += 10
                character["currentHP"] += 10
                slow_print(f"Your HP: {character['currentHP']} / {character['maxHP']}\n")
                break
            elif mystery_potion > 6:
                slow_print("Why are you drinking random shit off the ground? You deserve this. Lose 15 maxHP.")
                character["maxHP"] -= 15
                character["currentHP"] -= 15
                slow_print(f"Your HP: {character['currentHP']} / {character['maxHP']}\n")
                break
        elif user_input == 'n':
            slow_print("You decide to not drink the unknown liquid and throw the vial onto the ground.\n"
                       "Mom did always say to not eat anything you find in the streets...\n")
            break
        else:
            slow_print("\nInvalid input. Please enter either 'y' or 'n'.\n")
    # remove treasure event after event finishes
    board[(character["x-position"], character["y-position"])] = '^'


def check_exp(character) -> None:
    """
    Check if currentEXP is higher than or equal to maxEXP.

    If it is, change stats accordingly. Nothing happens otherwise.

    :param character: a dictionary
    :precondition character: a dictionary of character
    :postcondition: level up the character and increase stats 

    >>> character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
    ...              "maxEXP": 50, "currentEXP": 65, "atk": 5, "move": "Magic Missile",
    ...              "x-position": 10, "y-position": 20, "orb": 0}

    >>> check_exp(character_test)
    <BLANKLINE>
    You have leveled up! You are now level 2. You feel stronger, as the aura around you settles down.
    Your new stats --- HP: 110 / 110 --- ATK: 6 --- EXP: 15 / 55
    <BLANKLINE>

    >>> character_test['currentEXP'] = 40
    >>> check_exp(character_test)

    """
    while character["currentEXP"] >= character["maxEXP"]:
        character["level"] += 1
        character["currentEXP"] = int(character["currentEXP"] - character["maxEXP"])
        character["maxEXP"] = int(character["maxEXP"] * 1.1)
        character["currentHP"] = int(character["currentHP"] * 1.1)
        character["maxHP"] = int(character["maxHP"] * 1.1)
        character["atk"] = int(math.ceil(character["atk"] * 1.1))
        slow_print(f"\nYou have leveled up! You are now level {character['level']}. "
                   f"You feel stronger, as the aura around you settles down.")
        slow_print(f"Your new stats --- HP: {character['currentHP']} / {character['maxHP']} --- "
                   f"ATK: {character['atk']} --- EXP: {character['currentEXP']} / {character['maxEXP']}\n")


def healing_altar(character) -> None:
    """
    Heal the character to full HP
    
    :param character: a dictionary
    :precondition character: a dictionary with strings as keys and values
    :postcondition: heals the character to full HP

    >>> character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 50, "gold": 100, "level": 1,
    ...              "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
    ...              "x-position": 10, "y-position": 20, "orb": 0}
    >>> healing_altar(character_test)
    <BLANKLINE>
    You are at the healing altar. Heal yourself to full.
    You now have 100 / 100 HP.
    <BLANKLINE>

    >>> character_test["currentHP"] = 100
    >>> healing_altar(character_test)
    <BLANKLINE>
    You are at the healing altar. Heal yourself to full.
    You now have 100 / 100 HP.
    <BLANKLINE>
    """
    character["currentHP"] = character["maxHP"]
    slow_print("\nYou are at the healing altar. Heal yourself to full.\n"
               f"You now have {character['currentHP']} / {character['maxHP']} HP.\n")


def combat(character, enemy) -> None:
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
            slow_print(f"You rolled the die of fate... to roll {user_roll}!\n", 0.035)
            damage = character["atk"] * user_roll
            enemy["currentHP"] -= damage
            slow_print(f"You used {character['move']}!", delay=0.025)
            slow_print(f"You dealt {damage} damage to {enemy['name']}!", delay=0.025)
            slow_print(f"{enemy['name']}'s HP: {enemy['currentHP']} / {enemy['maxHP']}\n", delay=0.025)
            if enemy["currentHP"] > 0:
                character["currentHP"] -= enemy["atk"]
                slow_print(f"{enemy['name']} uses {enemy['move']}!", delay=0.025)
                slow_print(f"{enemy['name']} attacked you for {enemy['atk']}.", delay=0.025)
                slow_print(f"Your HP: {character['currentHP']} / {character['maxHP']}\n")
            else:
                character["gold"] += enemy["gold"]
                character["currentEXP"] += enemy["EXP"]
                slow_print(f"You have slain the {enemy['name']}!")
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
                slow_print("You cannot run from a boss fight. Just die in battle.\n")
        else:
            slow_print("Not a valid command! Choose from attack('x') or run('z').")


def combat_andromalius(character, board) -> None:
    """
    Trigger a combat event with Andromalius
    
    :param character: a dictionary
    :param board: a dictionary
    :precondition character: a dictionary with strings as keys and values
    :precondition board: a dictionary with tuples as keys and strings as values
    :postcondition: triggers a combat event with Andromalius
    """
    slow_print("Each breath you take seems to pierce your lungs...", delay=0.1)
    slow_print("A demon in the figure of a man holding a serpent staff walks out of thin air...!", delay=0.1)
    combat(character, make_andromalius())
    slow_print(f"You gained a red orb, containing Andromalius' soul. You have no idea what to do with it.")
    character["orb"] += 1
    board[(character["x-position"], character["y-position"])] = '*'


def combat_marbas(character, board) -> None:
    """
    Trigger a combat event with Marbas
    
    :param character: a dictionary
    :param board: a dictionary
    :precondition character: a dictionary with strings as keys and values
    :precondition board: a dictionary with tuples as keys and strings as values
    :postcondition: triggers a combat event with Marbas
    """
    slow_print("Visible mist forms when you start breathing...", delay=0.1)
    slow_print("A hideous lich rises from the ground... ", delay=0.1)
    combat(character, make_marbas())
    slow_print(f"You gained a blue orb, containing Marbas' soul. You have no idea what to do with it.")
    character["orb"] += 1
    board[(character["x-position"], character["y-position"])] = '*'


def combat_baal(character, boss) -> None:
    """
    Trigger a combat event with Baal

    :param character: a dictionary
    :param boss: a dictionary
    :precondition character: a dictionary with strings as keys and values
    :precondition boss: a dictionary with strings as keys and values
    :postcondition: triggers a combat event with Baal
    
    """
    slow_print("The stifling air exerts pressure onto your shoulders...", delay=0.1)
    slow_print("A figure rises up from the throne. \nThe air trembles in fear.", delay=0.1)
    slow_print("Baal: HAHAHAHA!!! Finally a worthy opponent!!! Let us celebrate this moment..."
               "\n WITH A DUEL TO THE DEATH!!!!!!!!!!", delay=0.08)
    combat(character, boss)


def shop_event(character, shop) -> None:
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
        slow_print(f"{index}. Item name: {item['name']}, Price: {item['price']} gold, Quantity: {item['amount']} "
                   f"{item['effect']}")

    slow_print(f"\nYou currently have {character['gold']} gold.\n")
    while True:
        try:
            user_input = input("Enter the number of the item you wish to buy, or 'q' to quit: ")
            if user_input == 'q':
                slow_print("Thank you for your patronage.")
                break

            item_index = int(user_input) - 1
            selected_item = shop[item_index]

            if selected_item["amount"] <= 0:
                slow_print("Sorry, you already bought out those items.")
            elif selected_item["price"] > character["gold"]:
                slow_print("Come back with enough gold you swine!!! Nothing is free in my town!!!")
            else:
                character["gold"] -= selected_item["price"]
                selected_item["amount"] -= 1

                if "added_HP" in selected_item:
                    character["currentHP"] += selected_item["added_HP"]
                    character["maxHP"] += selected_item["added_HP"]
                    slow_print(f"You have purchased the {selected_item['name']}.")
                    slow_print(f"Your HP is now {character['currentHP']} / {character['maxHP']}.")
                elif "added_ATK" in selected_item:
                    character["atk"] += selected_item["added_ATK"]
                    character["move"] = selected_item["move_upgrade"]
                    slow_print(f"You have purchased the {selected_item['name']}.")
                    slow_print(f"Your ATK is now {character['atk']}.")
                    slow_print(f"You now attack with {character['move']}.")
                elif "added_EXP" in selected_item:
                    character["currentEXP"] += selected_item["added_EXP"]
                    slow_print(f"You have purchased the {selected_item['name']}.")
                    check_exp(character)

                slow_print(f"You now have {character['gold']} gold.")

        except ValueError:
            print("That is not within the list of choices in this shop. Try again.")
        except IndexError:
            print("That item number does not exist within our shop. Try again.")


def main():
    mob = {"name": "Legion Soldier", "currentHP": 300, "maxHP": 1000, "atk": 10, "EXP": 25, "gold": 5}
    character = {"name": "BoB", "maxHP": 100, "gold": 0, "level": 1,
                 "currentHP": 100, "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                 "x-position": 0, "y-position": 0, "model": "O"}
    print(character)
    print(mob)
    print(character)


if __name__ == "__main__":
    main()
