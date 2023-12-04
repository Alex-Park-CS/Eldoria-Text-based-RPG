def make_character():
    character = {"name": "BoB", "HP": 100, "MP": 100, "gold": 10, 
                 "skills": {"magic missile": [10, 10]},
                 "x-position": 10, "y-position": 20, "model": "O"}
    return character


def is_alive(character):
    """
    Checks if the character's HP is over 0

    :param character: a dictionary
    :precondition: a character that is within the game board
    :postcondition: determines if the character's HP > 0
    :return: a boolean value
    """
    if character["HP"] > 0:
        return True
    else:
        return False