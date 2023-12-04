# This is a sample Python script.
from helper_functions.character_module import make_character, is_alive
from helper_functions.movement_module import get_user_choice, validate_move, move_character
from helper_functions.display_for_users import print_board, describe_current_location


def make_board():
    """
    Create a game board using the rows and columns parameters.

    A teXt-base game board requires a number of rows and columns to create a virtual board where the players can
    move through. Each coordinate is denoted such as: (0,1), indicating the X position with the first number, and the
    y position with the second number. Each room has a description of one of "Empty room", "Ominous Hallway",
    "Room of Skulls", "Altar of Magic", which describe the type of room the player is in.

    :postcondition: create a game board according to ASCII art minimap in list form
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


def main():
    board = make_board()
    character = make_character()
    print_board(board)
    print(character)
    describe_current_location(board, character)
    while is_alive(character):
        print(describe_current_location(board, character), character['x-position'], ",", character['y-position'])
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
        else:
            print("Cannot escape the doom! Face your fears...")


if __name__ == '__main__':
    main()


