import random
import math
from helper_functions.create_entity import make_pre_lv_10_field_mobs, make_post_lv_10_field_mobs


def determine_event(board, character, shop):
    current_position = board[(character["x-position"], character["y-position"])]
    if current_position == '^' and chance_of_event(0.40):
        combat(character, make_pre_lv_10_field_mobs()[random.randint(0, 1)])
    elif current_position == '*' and chance_of_event(0.50):
        combat(character, make_post_lv_10_field_mobs()[random.randint(0, 1)])
    elif current_position == 'S':
        shop_event(character, shop)
    

def chance_of_event(probability):
    random_number = random.uniform(0, 1)

    if random_number <= probability:
        return True
    else:
        return False


def check_exp(character):
    if character["currentEXP"] >= character["maxEXP"]:
        character["level"] += 1
        character["currentEXP"] = int(character["currentEXP"] - character["maxEXP"])
        character["maxEXP"] = int(character["maxEXP"] * 1.1)
        character["currentHP"] = int(character["currentHP"] * 1.1)
        character["maxHP"] = int(character["maxHP"] * 1.1)
        character["atk"] = int(math.ceil(character["atk"] * 1.1))
        print(f"You have leveled up! You are now level {character['level']}. "
              f"You feel stronger, as the aura around you settles down.")
        print(f"Your new stats --- HP: {character['currentHP']} / {character['maxHP']} --- "
              f"ATK: {character['atk']} --- EXP: {character['currentEXP']} / {character['maxEXP']}")



def combat(character, enemy):
    print(f"\nYou have encountered a wild {enemy['name']}!!")
    while character["currentHP"] > 0 and enemy["currentHP"] > 0:
        print(f"Current Status->   Your HP: {character['currentHP']} / {character['maxHP']}   ", end="")
        print(f"{enemy['name']}'s HP: {enemy['currentHP']} / {enemy['maxHP']}\n")
        user_choice = input('Enter "x" to attack or "z" to run away: ')
        if user_choice == 'x':
            user_roll = random.randint(1, 12)
            print(f"You rolled the die of fate... to roll {user_roll}!\n")
            damage = character["atk"] * user_roll
            enemy["currentHP"] -= damage
            print(f"You used {character["move"]}!")
            print(f"You dealt {damage} damage to {enemy['name']}!")
            print(f"{enemy['name']}'s HP: {enemy['currentHP']} / {enemy['maxHP']}\n")
            if enemy["currentHP"] > 0:
                character["currentHP"] -= enemy["atk"]
                print(f"{enemy['name']} attacked you for {enemy['atk']}.")
                print(f"Your HP: {character['currentHP']} / {character['maxHP']}\n")
            else:
                character["gold"] += enemy["gold"]
                character["currentEXP"] += enemy["EXP"]
                print(f"You earned {enemy['gold']} gold! You now have {character['gold']} gold.")
                print(f"You earned {enemy['EXP']} XP! You now have {character['currentEXP']}/{character['maxEXP']} XP.\n\n")
                check_exp(character)
        elif user_choice == 'z':
            print("You run away, shrieking like a little girl. To think that the fate of "
                  "this world lies on the likes of you...\n")
            break

def shop_event(character, shop):
    print("Welcome, hero. I have travelled thousands of miles to be of assistance."
          "Here are the items that I have managed to bring for you."
          "But they aren't free. I still have to feed my family you know?\n")
    for index, item in enumerate(shop, start=1):
        print(f"{index}. Item name: {item['name']}, Price: {item['price']} gold, {item['effect']}")

    print(f"\nYou currently have {character["gold"]} gold.\n")
    while True:
        user_input = input("Enter the number of the item you wish to buy, or 'q' to quit: ")
        if user_input == '1':
            if shop[0]["amount"] <= 0:
                print("Sorry, you already bought out those items.")
            elif shop[0]["price"] > character["gold"]:
                print("Come back with enough gold you swine!!! Nothing is free in my town!!!")
            else:
                character["gold"] -= shop[0]["price"]
                shop[0]["amount"] -= 1
                character["currentHP"] += shop[0]["added_HP"]
                character["maxHP"] += shop[0]["added_HP"]
                print(f"You have purchased the {shop[0]["name"]}.")
                print(f"Your HP is now {character["currentHP"]} / {character["maxHP"]}.")
                print(f"You now have {character["gold"]} gold.")
        elif user_input == '2':
            if shop[1]["amount"] <= 0:
                print("Sorry, you already bought out those items.")
            elif shop[1]["price"] > character["gold"]:
                print("Come back with enough gold you swine!!! Nothing is free in my town!!!")
            else:
                character["gold"] -= shop[1]["price"]
                shop[1]["amount"] -= 1
                character["atk"] += shop[1]["added_ATK"]
                character["move"] = shop[1]["move_upgrade"]
                print(f"You have purchased the {shop[1]["name"]}.")
                print(f"Your ATK is now {character["atk"]}.")
                print(f"You now attack with {character["move"]}.")
                print(f"You now have {character["gold"]} gold.")
        elif user_input == '3':
            if shop[2]["amount"] <= 0:
                print("Sorry, you already bought out those items.")
            elif shop[2]["price"] > character["gold"]:
                print("Come back with enough gold you swine!!! Nothing is free in my town!!!")
            else:
                character["gold"] -= shop[2]["price"]
                shop[2]["amount"] -= 1
                character["currentEXP"] += shop[2]["added_EXP"]
                print(f"You have purchased the {shop[2]["name"]}.")
                check_exp(character)
                print(f"Your ATK is now {character["atk"]}.")
                print(f"You now have {character["gold"]} gold.")
        elif user_input == 'q':
            print("Thank you for your patronage.")
            break
        else:
            print("We don't sell anything like that... choose something else.")


    
    

def main():
    mob = {"name": "Legion Soldier", "currentHP": 300, "maxHP": 1000, "atk": 10, "EXP": 25, "gold": 5}
    character = {"name": "BoB", "maxHP": 100, "gold": 0, "level": 1,
                 "currentHP": 100, "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                 "x-position": 10, "y-position": 20, "model": "O"}
    print(character)

    combat(character, mob)

    print(character)


if __name__ == "__main__":
    main()
