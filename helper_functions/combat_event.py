import random


def combat(character, enemy):
    print(f"You have encountered a wild {enemy['name']}!!")
    while character["currentHP"] > 0 and enemy["currentHP"] > 0:
        print(f"Current Status->   Your HP: {character['currentHP']} / {character['maxHP']}   ", end="")
        print(f"{enemy['name']}'s HP: {enemy['currentHP']} / {enemy['maxHP']}\n")
        user_choice = input('Enter "a" to attack or "r" to run away: ')
        if user_choice == 'a':
            user_roll = random.randint(1, 12)
            print(f"You rolled the die of fate... to roll {user_roll}!\n")
            damage = character["atk"] * user_roll
            enemy["currentHP"] -= damage
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
                print(f"You earned {enemy['EXP']} XP! You now have {character['currentEXP']}/{character['maxEXP']} XP.")
        elif user_choice == 'r':
            print("You run away, shrieking like a little girl. To think that the fate of "
                  "this world lies on the likes of you...")
            break


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