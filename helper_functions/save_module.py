import json
from ast import literal_eval


def dict_to_json_string_conversion(board):
    """

    :param board:
    :return:
    """
    if type(list(board.keys())[0]) == tuple:
        converted = {str(key): value for key, value in board.items()}
    else:
        converted = {literal_eval(key): value for key, value in board.items()}

    return converted


def save_game_character(character):
    """
    Save the current game state to a JSON file in the specified directory.

    :param:
    :precondition:
    :postcondition:

    """

    directory = "saves\\save_character.json"

    with open(directory, "w") as character_file:
        json.dump(character, character_file, indent=4)

    print(f"Character saved successfully to {directory}!")


def save_game_board(board):
    """

    :param board:
    :return:
    """
    directory = "saves\\save_board.json"
    converted_board = dict_to_json_string_conversion(board)
    with open(directory, "w") as board_file:
        json.dump(converted_board, board_file, indent=4)

    print(f"Game board saved successfully to {directory}!")


def save_shop(shop):
    """
    Save the current game state to a JSON file in the specified directory.

    :param:
    :precondition:
    :postcondition:

    """

    directory = "saves\\save_shop.json"

    with open(directory, "w") as shop_file:
        json.dump(shop, shop_file, indent=4)

    print(f"Shop saved successfully to {directory}!")


def load_game_character():
    """
    Load the saved JSON file as a dictionary into a character variable
    :return:
    """
    char = {}
    directory = "saves\\save_character.json"
    try:
        with open(directory, 'r') as char_info:
            char = json.load(char_info)
    except FileNotFoundError:
        print("Save file not found. Creating a new character...")

    return char


def load_game_board():
    """
    Load the saved JSON file as a dictionary into a board variable
    :return:
    """
    game_bd = {}
    directory = "saves\\save_board.json"
    try:
        with open(directory, 'r') as bd_info:
            game_bd = json.load(bd_info)
    except FileNotFoundError:
        print("Save file not found. Creating a new board...")

    return dict_to_json_string_conversion(game_bd)


def load_game_shop():
    """
    Load the saved JSON file as a dictionary into a character variable
    :return:
    """
    shop = {}
    directory = "saves\\save_shop.json"
    try:
        with open(directory, 'r') as shop_info:
            shop = json.load(shop_info)
    except FileNotFoundError:
        print("Save file not found. Creating a new shopkeeper...")

    return shop
