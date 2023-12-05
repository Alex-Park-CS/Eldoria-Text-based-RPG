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
