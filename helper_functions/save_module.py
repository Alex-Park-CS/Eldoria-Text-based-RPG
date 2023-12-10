import json
from ast import literal_eval


def dict_to_json_string_conversion(board) -> dict:
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
    {(1, 2): 'X', (3, 4): 'O'}
    """
    if type(list(board.keys())[0]) == tuple:
        converted = {str(key): value for key, value in board.items()}
    else:
        converted = {literal_eval(key): value for key, value in board.items()}

    return converted


def save_game_character(character) -> None:
    """
    Save the current game state to a JSON file in the specified directory.

    :param character: a dictionary 
    :precondition: the dictionary keys are strings
    :postcondition: dictionary is saved as a JSON file
    :raises FileNotFoundError: if the character save file cannot be found

    >>> test_dict = {'name': 'Ysera', 'maxHP': 100, 'currentHP': 100, 'gold': 100, 'level': 1}
    >>> save_game_character(test_dict)
    Character game file cannot be found! Exiting.
    """
    directory = "saves\\save_character.json"
    try:
        with open(directory, "w") as character_file:
            json.dump(character, character_file, indent=4)

        print(f"Character saved successfully to {directory}!")
    except FileNotFoundError:
        print("Character game file cannot be found! Exiting.")


def save_game_board(board) -> None:
    """
    Save the current game state to a JSON file in the specified directory.

    :param board: a dictionary
    :precondition: the dictionary keys are strings
    :postcondition: dictionary is saved as a JSON file
    :raises FileNotFoundError: if the game board save file cannot be found

    >>> test_dict = {'(0, 0)': 'X', '(0, 1)': 'X', '(0, 2)': ' ', '(0, 3)': 'X', '(1, 0)': ' '}
    >>> save_game_board(test_dict)
    Game board file cannot be found! Exiting.

    """

    directory = "saves\\save_board.json"
    converted_board = dict_to_json_string_conversion(board)
    try:
        with open(directory, "w") as board_file:
            json.dump(converted_board, board_file, indent=4)

        print(f"Game board saved successfully to {directory}!")
    except FileNotFoundError:
        print("Game board file cannot be found! Exiting.")


def save_shop(shop) -> None:
    """
    Save the current game state to a JSON file in the specified directory.

    :param shop: a dictionary
    :precondition: the dictionary keys are strings
    :postcondition: dictionary is saved as a JSON file
    :raises FileNotFoundError: if the shop save file cannot be found
    """

    directory = "saves\\save_shop.json"
    try:
        with open(directory, "w") as shop_file:
            json.dump(shop, shop_file, indent=4)

        print(f"Shop saved successfully to {directory}!")
    except FileNotFoundError:
        print("Game shop file cannot be found! Exiting.")


def load_game_character() -> dict:
    """
    Load the saved JSON file as a dictionary into a character variable

    :precondition: the json object keys are strings
    :postcondition: the json object is changed to a dictionary data type
    :return: a dictionary
    :raises FileNotFoundError: if the character save file cannot be found
    """
    char = {}
    directory = "saves\\save_character.json"
    try:
        with open(directory, 'r') as char_info:
            char = json.load(char_info)
    except FileNotFoundError:
        print("Save file not found. Creating a new character...")

    return char


def load_game_board() -> dict:
    """
    Load the saved JSON file as a dictionary into a board variable
    
    :precondition: the json object keys are strings
    :postcondition: the json object keys are tuples
    :return: a dictionary
    :raises FileNotFoundError: if the game board save file cannot be found
    """
    game_bd = {}
    directory = "saves\\save_board.json"
    try:
        with open(directory, 'r') as bd_info:
            game_bd = json.load(bd_info)
    except FileNotFoundError:
        print("Save file not found. Creating a new board...")

    return dict_to_json_string_conversion(game_bd)


def load_game_shop() -> dict:
    """
    Load the saved JSON file as a dictionary into a shop variable

    :precondition: the json object keys are strings
    :postcondition: the json object is changed to a dictionary data type
    :return: a dictionary
    :raises FileNotFoundError: if the shop save file cannot be found
    """
    shop = {}
    directory = "saves\\save_shop.json"
    try:
        with open(directory, 'r') as shop_info:
            shop = json.load(shop_info)
    except FileNotFoundError:
        print("Save file not found. Creating a new shopkeeper...")

    return shop
