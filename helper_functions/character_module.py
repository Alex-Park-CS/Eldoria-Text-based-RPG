from helper_functions.create_entity import make_character


def is_alive(character) -> bool:
    """
    Checks if the character's HP is over 0

    :param character: a dictionary
    :precondition: a character that is within the game board
    :postcondition: determines if the character's HP > 0
    :return: a boolean value

    >>> character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
    ...              "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
    ...              "x-position": 10, "y-position": 20, "orb": 0}
    
    >>> is_alive(character_test)
    True

    >>> character_test["currentHP"] = 0
    >>> is_alive(character_test)
    False

    """
    if character["currentHP"] > 0:
        return True
    else:
        return False


def main():
    character = make_character()
    life_check_character = is_alive(character)
    print(life_check_character)


if __name__ == "__main__":
    main()
