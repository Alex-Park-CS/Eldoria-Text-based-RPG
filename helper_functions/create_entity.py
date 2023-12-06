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
                    "X***XXXXXX-XXXXXX***X",
                    "X                   X",
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
                    "XXXXXXXXX   XXXXXXXXX"]

    map_dict = {}
    for x, row in enumerate(map_of_board):
        for y, char in enumerate(row):
            map_dict[(y, x)] = char
    return map_dict


def make_character():
    character = {"name": "BoB", "maxHP": 100, "currentHP": 100, "gold": 300, "level": 1,
                 "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                 "x-position": 10, "y-position": 20, "souls": 0}
    return character


def make_pre_lv_10_field_mobs():
    soldier = {"name": "Legion Soldier", "currentHP": 100, "maxHP": 100,
               "atk": 10, "EXP": 25, "gold": 20, "runnable": True}
    mutant_boar = {"name": "Mutant Boar", "currentHP": 50, "maxHP": 50,
                   "atk": 5, "EXP": 10, "gold": 5, "runnable": True}
    list_of_pre_lvl_10_mobs = [mutant_boar, soldier]
    return list_of_pre_lvl_10_mobs


def make_post_lv_10_field_mobs():
    imp = {"name": "Imp", "currentHP": 100, "maxHP": 100, "atk": 15, "EXP": 25, "gold": 20, "runnable": True}
    commander = {"name": "Legion Commander", "currentHP": 400, "maxHP": 400,
                 "atk": 20, "EXP": 60, "gold": 75, "runnable": True}
    list_of_post_lvl_10_mobs = [imp, commander]
    return list_of_post_lvl_10_mobs


def make_beginner_shop():
    pill_of_vitality = {"name": "Pill of Vitality", "price": 50, "added_HP": 30,
                        "amount": 1, "effect": "Increases maxHP by 30 points"}
    elixir_of_vigor = {"name": "Elixer of Vigor", "price": 65, "added_ATK": 10,
                       "move_upgrade": "Arcane Barrage", "amount": 1,
                       "effect": "Increases ATK by 10 points"}
    forbidden_powder = {"name": "Forbidden White Powder", "price": 40, "added_EXP": 100, 
                        "amount": 2, "effect": "Increases currentEXP by 100 points"}
    list_of_items = [pill_of_vitality, elixir_of_vigor, forbidden_powder]
    return list_of_items
