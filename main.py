# This is a sample Python script.
import random
from character.character_module import make_character, is_alive
from character_movement.movement_module import get_user_choice, validate_move, move_character
from user_display.display_for_users import print_board, describe_current_location


def make_board():
    """
    Create a game board using the rows and columns parameters.

    A teXt-base game board requires a number of rows and columns to create a virtual board where the players can
    move through. Each coordinate is denoted such as: (0,1), indicating the X position with the first number, and the
    y position with the second number. Each room has a description of one of "Empty room", "Ominous Hallway",
    "Room of Skulls", "Altar of Magic", which describe the type of room the player is in.

    :param rows: positive, non-zero integer
    :param columns: another positive, non-zero integer
    :precondition rows: must be an integer greater than or equal to 2
    :precondition columns: must be also an integer greater than or equal to 2
    :postcondition: create a game board which has the number of rows and columns as given in the parameters; each
    coordinate has a room description
    :return: a dictionary with tuples as the keys, and strings as values

    """
    map_of_board = ["XXXXXXXXXXXXXXXXXXXXX",
                    "XXXXXXXXXXXXXXXXXXXXX",
                    "X*****MCX B XCM*****X",
                    "X******X     X******X",
                    "X*****X       X*****X",
                    "X****X         X****X",
                    "X***XXXXXXKXXXXXX***X",
                    "X                  ZX",
                    "X********* ********HX",
                    "XXXXXXXXXX XXXXXXXXXX",
                    "XXXXXXXXXX/XXXXXXXXXX",
                    "XH   ^   S         HX",
                    "X   ^ ^         ^   X",
                    "X^^X^^X^    ^ ^  ^  X",
                    "X ^^^^^^            X",
                    "X^XXXTXX    ^ ^     X",
                    "X ^^^XX^         ^  X",
                    "X ^^^^^^     ^      X",
                    "X^  ^ ^           ^ X",
                    "X  ^  ^             X",
                    "XXXXXXXXXXOXXXXXXXXXX"]

    map_dict = {}
    for x, row in enumerate(map_of_board):
        for y, char in enumerate(row):
            map_dict[(x, y)] = char
    return map_dict

def get_user_choice():
    """
    Get input direction from user in numbers.

    The input will be integers which signify direction where 1 = North, 2 = West, 3 = South, 4 = East
    :postcondition: the user input direction in integer
    :return: an integer

    """
    list_choice = ('1', '2', '3', '4')
    user_direction = '0'
    while user_direction not in list_choice:
        user_direction = input("Enter a number for a direction from North(1), West(2), South(3), East(4): ").strip()
        if user_direction in list_choice:
            return user_direction
        else:
            print("Read instructions again...")



def main():
    board = make_board()
    character = make_character()
    print_board(board)
    print(character)
    while is_alive(character):
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            

    


if __name__ == '__main__':
    main()


