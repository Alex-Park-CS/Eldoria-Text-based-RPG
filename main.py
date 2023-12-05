# This is a sample Python script.
from helper_functions.character_module import is_alive
from helper_functions.movement_module import get_user_choice, validate_move, move_character
from helper_functions.display_for_users import print_board, describe_current_location
from helper_functions.create_entity import make_character, make_board
from helper_functions.special_events import determine_event, check_exp


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
            determine_event(board, character)
        else:
            print("You cannot go there. Try again.")
        print_board(board, character)


if __name__ == '__main__':
    main()


