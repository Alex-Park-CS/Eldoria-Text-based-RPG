# This is a sample Python script.
from helper_functions.character_module import is_alive
from helper_functions.movement_module import get_user_choice, validate_move, move_character
from helper_functions.display_for_users import (
    print_board,
    intro_prompt,
    slow_print,
    print_character_stats)
from helper_functions.create_entity import make_character, make_board, make_shop, make_baal
from helper_functions.special_events import determine_event


def main():
    board = make_board()
    character = make_character()
    shop = make_shop()
    boss = make_baal()
    user_choice = ''
    slow_print(intro_prompt(), delay=0.001)
    print_board(board, character)
    print_character_stats(character)
    while is_alive(character) and boss["currentHP"] > 0 and user_choice != 'q':
        try:
            direction = get_user_choice()
        except ValueError as e:
            print(e)
            continue
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            determine_event(board, character, shop, boss)
            print_board(board, character)
        else:
            print("You cannot go there. Try again.")

    if(character["currentHP"]) <= 0:
        print("You died... The world falls to the hands of Baal, the new supreme leader of the world! All hail Baal!!")
    else:
        print("You have saved the world hero!! Thank you!!")


if __name__ == '__main__':
    main()
