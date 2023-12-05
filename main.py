# This is a sample Python script.
from helper_functions.character_module import is_alive, check_exp
from helper_functions.movement_module import get_user_choice, validate_move, move_character
from helper_functions.display_for_users import print_board, describe_current_location
from helper_functions.create_entity import make_character, make_board, make_imp, make_legion_commander, make_legion_soldier, make_mutant_boar


def main():
    board = make_board()
    character = make_character()
    print_board(board, character)
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
        print_board(board, character)


if __name__ == '__main__':
    main()


