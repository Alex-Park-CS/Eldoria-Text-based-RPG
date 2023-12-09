import json
from ast import literal_eval


def dict_to_json_string_conversion(board):
    """
    Convert the dictionary keys from tuples to strings so that it can be saved as a JSON file.

    :param board: a dictionary
    :precondition: the dictionary keys are tuples
    :postcondition: the dictionary keys are strings
    :return: a dictionary with string keys

    >>> test_dict = {(1, 2): 'X', (3, 4): 'O'}
    >>> dict_to_json_string_conversion(test_dict)
    {'(1, 2)': 'X', '(3, 4)': 'O'}

    >>> test_dict = {'(1, 2)': 'X', '(3, 4)': 'O'}
    >>> dict_to_json_string_conversion(test_dict)
    {'(1, 2)': 'X', '(3, 4)': 'O'}
    """
    if type(list(board.keys())[0]) == tuple:
        converted = {str(key): value for key, value in board.items()}
    else:
        converted = {literal_eval(key): value for key, value in board.items()}

    return converted


def save_game_character(character):
    """
    Save the current game state to a JSON file in the specified directory.

    :param character: a dictionary 
    :precondition: the dictionary keys are strings
    :postcondition: dictionary is saved as a JSON file

    >>> test_dict = {'name': 'Ysera', 'maxHP': 100, 'currentHP': 100, 'gold': 100, 'level': 1}
    >>> save_game_character(test_dict)
    Character saved successfully to saves\\save_character.json!


    """

    directory = "saves\\save_character.json"

    with open(directory, "w") as character_file:
        json.dump(character, character_file, indent=4)

    print(f"Character saved successfully to {directory}!")


def save_game_board(board):
    """
    Save the current game state to a JSON file in the specified directory.

    :param board: a dictionary
    :precondition: the dictionary keys are strings
    :postcondition: dictionary is saved as a JSON file

    >>> test_dict = {'(0, 0)': 'X', '(0, 1)': 'X', '(0, 2)': ' ', '(0, 3)': 'X', '(1, 0)': ' '}
    >>> save_game_board(test_dict)
    Game board saved successfully to saves\\save_board.json!

    """
    directory = "saves\\save_board.json"
    converted_board = dict_to_json_string_conversion(board)
    with open(directory, "w") as board_file:
        json.dump(converted_board, board_file, indent=4)

    print(f"Game board saved successfully to {directory}!")


def save_shop(shop):
    """
    Save the current game state to a JSON file in the specified directory.

    :param shop: a dictionary
    :precondition: the dictionary keys are strings
    :postcondition: dictionary is saved as a JSON file

    >>> test_dict = {'(0, 0)': 'X', '(0, 1)': 'X', '(0, 2)': ' ', '(0, 3)': 'X', '(1, 0)': ' ', '(1, 1)': 'X'
    >>> save_shop(test_dict)
    Shop saved successfully to saves\\save_shop.json!
    """

    directory = "saves\\save_shop.json"

    with open(directory, "w") as shop_file:
        json.dump(shop, shop_file, indent=4)

    print(f"Shop saved successfully to {directory}!")


def load_game_character():
    """
    Load the saved JSON file as a dictionary into a character variable

    :precondition: the json object keys are strings
    :postcondition: the json object is changed to a dictionary data type
    :return: a dictionary
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
    
    :precondition: the json object keys are strings
    :postcondition: the json object keys are tuples
    :return: a dictionary
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
    Load the saved JSON file as a dictionary into a shop variable

    :precondition: the json object keys are strings
    :postcondition: the json object is changed to a dictionary data type
    :return: a dictionary
    """
    shop = {}
    directory = "saves\\save_shop.json"
    try:
        with open(directory, 'r') as shop_info:
            shop = json.load(shop_info)
    except FileNotFoundError:
        print("Save file not found. Creating a new shopkeeper...")

    return shop
