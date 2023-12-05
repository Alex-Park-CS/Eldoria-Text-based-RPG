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
                    "XXXXXXXXXX XXXXXXXXXX"]

    map_dict = {}
    for x, row in enumerate(map_of_board):
        for y, char in enumerate(row):
            map_dict[(y, x)] = char
    print(map_dict)
    return map_dict


def make_character():
    character = {"name": "BoB", "maxHP": 100, "gold": 0, "level": 1,
                 "currentHP": 100, "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                 "x-position": 10, "y-position": 20, "model": "O"}
    return character


def make_pre_lv_10_field_mobs():
    soldier = {"name": "Legion Soldier", "currentHP": 100, "maxHP": 100, "atk": 10, "EXP": 25, "gold": 20}
    mutant_boar = {"name": "Mutant Boar", "currentHP": 50, "maxHP": 50, "atk": 5, "EXP": 10, "gold": 5}
    list_of_pre_lvl_10_mobs = [mutant_boar, soldier]
    return list_of_pre_lvl_10_mobs


def make_post_lv_10_field_mobs():
    imp = {"name": "Imp", "currentHP": 100, "maxHP": 100, "atk": 15, "EXP": 25, "gold": 20}
    commander = {"name": "Legion Commander", "currentHP": 400, "maxHP": 400, "atk": 20, "EXP": 60, "gold": 75}
    list_of_post_lvl_10_mobs = [imp, commander]
    return list_of_post_lvl_10_mobs
