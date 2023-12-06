from helper_functions.display_for_users import print_character_stats


def get_user_choice():
    """
    Get input direction from user in numbers.

    The input will be integers which signify direction where 1 = North, 2 = West, 3 = South, 4 = East, q = Quit
    :postcondition: the user input direction in integer
    :return: an integer

    """
    list_choice = ('w', 'a', 's', 'd', 'k', 'q')
    user_direction = '0'
    while user_direction not in list_choice:
        user_direction = input("Enter the desired direction from North(w), "
                               "West(a), South(s), East(d), Stats(k), or 'q' to quit: ").strip().lower()
        if user_direction in list_choice:
            return user_direction
        else:
            raise ValueError("Invalid input. This input is not within the choices.\n")
            

def validate_move(board, character, user_direction):
    """
    Check if the user's direction is within the bounds of the board.

    Validates the user choice and returns True if the user chosen direction can be actually reached.
    :param board: a dictionary
    :param character: another dictionary
    :param user_direction: a string
    :precondition board: a game board dictionary
    :precondition character: a character dictionary
    :precondition user_direction: a string indicating the direction or special command(k, q)
    :postcondition: validate if the character can go to the desired direction
    :return: boolean value

    >>> character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
    ...              "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
    ...              "x-position": 10, "y-position": 15, "orb": 0}

    """

    if user_direction == 'w':
        if ((character["x-position"], character["y-position"] - 1) in board
                and board[(character["x-position"], character["y-position"] - 1)] != 'X'):
            return True
        else:
            return False
    elif user_direction == 'a':
        if ((character["x-position"] - 1, character["y-position"]) in board and
                board[(character["x-position"] - 1, character["y-position"])] != 'X'):
            return True
        else:
            return False
    elif user_direction == 's':
        if ((character["x-position"], character["y-position"] + 1) in board and
                board[(character["x-position"], character["y-position"] + 1)] != 'X'):
            return True
        else:
            return False
    elif user_direction == 'd':
        if ((character["x-position"] + 1, character["y-position"]) in board and
                board[(character["x-position"] + 1, character["y-position"])] != 'X'):
            return True
        else:
            return False
    elif user_direction == 'k':
        print_character_stats(character)
        return False
    else:
        return False


def move_character(character, user_direction):
    """
    Move character according to the user direction

    :param character: a dictionary
    :param user_direction: a string
    :precondition character: a character that is not dead (have 0 HP)
    :precondition integer: a string with a direction that is accessible
    :postcondition: change the character's position according to the user given direction

    >>> character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
    ...              "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
    ...              "x-position": 10, "y-position": 20, "orb": 0}
    >>> move_character(character_test, 'w')
    >>> character_test["y-position"]
    19
    >>> move_character(character_test, 'a')
    >>> character_test["x-position"]
    9
    """
    if user_direction == 'w':
        character["y-position"] -= 1
    elif user_direction == 'a':
        character["x-position"] -= 1
    elif user_direction == 's':
        character["y-position"] += 1
    elif user_direction == 'd':
        character["x-position"] += 1


def main():
    # user_direction = "w"
    # character = {"x-position": 5, "y-position": 5}tilte
    print("hello")


if __name__ == "__main__":
    main()
