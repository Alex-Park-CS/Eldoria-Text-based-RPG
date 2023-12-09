from helper_functions.character_module import is_alive
from helper_functions.movement_module import get_user_choice, validate_move, move_character
from helper_functions.display_for_users import (
    print_board,
    intro_prompt,
    slow_print,
    print_character_stats)
from helper_functions.create_entity import make_board, make_shop, make_baal, make_character
from helper_functions.special_events import (
    determine_event,
    save_game_character,
    load_game_character,
    save_game_board,
    load_game_board)


def main():
    board = {}
    character = {}
    user_choice = input("Choose 1 to load save file, or 2 to create new game: ")
    if user_choice == '1':
        character = load_game_character()
        board = load_game_board()
    elif user_choice == '2':
        character = make_character()
        board = make_board()
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
        user_choice = direction
        if user_choice == 'q':
            break
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            try:
                determine_event(board, character, shop, boss)
            except ValueError as e:
                print(e)
            print_board(board, character)
        else:
            print("You cannot go there. Try again.")

    if user_choice == 'q':
        save_game_character(character)
        save_game_board(board)
        slow_print("You have quit the game. Goodbye!")
    elif(character["currentHP"]) <= 0:
        slow_print("You died... The world falls to the hands of Baal, "
                   "the new supreme leader of the world! All hail Baal!!")
    else:
        slow_print("You have saved the world hero!! Thank you!!")


if __name__ == '__main__':
    main()
