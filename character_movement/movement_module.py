def get_user_choice():
    """
    Get input direction from user in numbers.

    The input will be integers which signify direction where 1 = North, 2 = West, 3 = South, 4 = East, q = Quit
    :postcondition: the user input direction in integer
    :return: an integer

    """
    list_choice = ('1', '2', '3', '4', 'Q')
    user_direction = '0'
    while user_direction not in list_choice:
        user_direction = input("Enter a number for a direction from North(1), West(2), South(3), East(4), or 'Q' to quit: ").strip()
        if user_direction in list_choice:
            return user_direction
        else:
            print("Read instructions again...")
            

def validate_move(board, character, user_direction):
    """
    Check if the user's direction is within the bounds of the board.

    Validates the user choice and returns True if the user chosen direction can be actually reached.
    :param board: a dictionary
    :param character: another dictionary
    :param user_direction: a string
    :precondition board: a game board with row and columns >= 2
    :precondition character: a character
    :precondition user_direction: a string between and including 1 and 4
    :postcondition: validate if the character can go to the desired direction
    :return: boolean value

    >>> game_board = {(0, 0): "Empty Room", (0, 1): "Empty Room", (1, 0): "Empty Room", (1, 1): "Empty Room"}
    >>> game_character = {"x-position": 0, "y-position": 0, "HP": 5}
    >>> validate_move(game_board, game_character, '3')
    True

    >>> game_board = {(0, 0): "Empty Room", (0, 1): "Empty Room", (1, 0): "Empty Room", (1, 1): "Empty Room"}
    >>> game_character = {"x-position": 0, "y-position": 0, "HP": 5}
    >>> validate_move(game_board, game_character, '2')
    False
    """

    if user_direction == '1':
        if (character["x-position"], character["y-position"] - 1) in board and board[(character["x-position"], character["y-position"] - 1)] != 'X':
            print("North")
            return True
        else:
            print((character["x-position"], character["y-position"] - 1))
            return False
    elif user_direction == '2':
        if (character["x-position"] - 1, character["y-position"]) in board and board[(character["x-position"] - 1, character["y-position"])] != 'X':
            return True
        else:
            return False
    elif user_direction == '3':
        if (character["x-position"], character["y-position"] + 1) in board and board[(character["x-position"], character["y-position"] + 1)] != 'X':
            return True
        else:
            return False
    elif user_direction == '4':
        if (character["x-position"] + 1, character["y-position"]) in board and board[(character["x-position"] + 1, character["y-position"])] != 'X':
            return True
        else:
            return False
        
def move_character(character, user_direction):
    """
    Move character according to the user direction

    :param character: a dictionary
    :param user_direction: a string
    :precondition character: a character that is not dead (have 0 HP)
    :precondition integer: an string with a direction that is accessible
    :postcondition: change the character's position according to the user given direction

    # >>> character_test = {"x-position": 0, "y-position": 0, "HP" 5}
    # >>> user_direction_test = 3
    # >>> move_character(character_test, user_direction_test)

    """
    if user_direction == '1':
        character["y-position"] -= 1
    elif user_direction == '2':
        character["x-position"] -= 1
    elif user_direction == '3':
        character["y-position"] += 1
    else:
        character["x-position"] += 1