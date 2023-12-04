def make_character():
    character = {"name": "BoB", "maxHP": 100, "gold": 0, "level": 1,
                 "currentHP": 100, "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                 "x-position": 10, "y-position": 20, "model": "O"}
    return character


def check_exp(character):
    if character["currentEXP"] >= character["maxEXP"]:
        character["level"] += 1
        character["currentEXP"] -= character["maxEXP"]
        character["maxEXP"] *= 1.2
        character["currentHP"] *= 1.2
        character["maxHP"] *= 1.2
        character["atk"] *= 1.5
        print("You have leveled up!")


def is_alive(character):
    """
    Checks if the character's HP is over 0

    :param character: a dictionary
    :precondition: a character that is within the game board
    :postcondition: determines if the character's HP > 0
    :return: a boolean value
    """
    if character["currentHP"] > 0:
        return True
    else:
        return False
