def make_board() -> dict:
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
                    "X*****AXX B XXM*****X",
                    "X******X     X******X",
                    "X*****X       X*****X",
                    "X****X         X****X",
                    "X***XXXXXX-XXXXXX***X",
                    "X                   X",
                    "X********* ********HX",
                    "XXXXXXXXXX XXXXXXXXXX",
                    "XXXXXXXXXX/XXXXXXXXXX",
                    "XH   ^   S         HX",
                    "X   ^ ^         X^X X",
                    "X^^X^^X^    ^ ^  ^X^X",
                    "X ^^^^^^       XXXX X",
                    "X^XXXTXX    ^X^XT^  X",
                    "X ^^^XX^     XXXXXXXX",
                    "X ^^^^^^     ^      X",
                    "X^  ^ ^           ^ X",
                    "X  ^  ^             X",
                    "XXXXXXXXX   XXXXXXXXX"]

    map_dict = {(y, x): char for x in range(len(map_of_board[0]))
                for y in range(len(map_of_board))
                for char in map_of_board[x][y]}
    return map_dict


def make_character() -> dict:
    """
    Create a character dictionary with the following keys: name, maxHP, currentHP, gold, level, maxEXP, currentEXP,
    atk, move, x-position, y-position, orb.
    
    :postcondition: create a character dictionary with the character stats
    :return: a dictionary with the character stats
    
    >>> make_character()
    {'name': 'Ysera', 'maxHP': 100, 'currentHP': 100, 'gold': 100, 'level': 1, 'maxEXP': 50, 
    'currentEXP': 0, 'atk': 5, 'move': 'Magic Missile', 'x-position': 10, 'y-position': 20, 'orb': 0}

    """
    character = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                 "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                 "x-position": 10, "y-position": 20, "orb": 0}
    return character


def make_pre_lv_10_field_mobs() -> list:
    """
    Create a list of dictionaries of pre-level 10 field mobs with the following keys: name, currentHP, maxHP, atk,
    move, EXP, gold, runnable.
    
    :postcondition: create a list of dictionaries of pre-level 10 field mobs
    :return: a list of dictionaries of pre-level 10 field mobs
    
    >>> make_pre_lv_10_field_mobs()
    [{'name': 'Mutant Boar', 'currentHP': 50, 'maxHP': 50, 'atk': 5, 'move': 'Headbutt', 'EXP': 10, 'gold': 5,
    'runnable': True}, {'name': 'Legion Soldier', 'currentHP': 100, 'maxHP': 100, 'atk': 10, 'move': 'Spear Thrust',
    'EXP': 25, 'gold': 20, 'runnable': True}]
    """
    soldier = {"name": "Legion Soldier", "currentHP": 100, "maxHP": 100, "move": "Spear Thrust",
               "atk": 10, "EXP": 25, "gold": 20, "runnable": True}
    mutant_boar = {"name": "Mutant Boar", "currentHP": 50, "maxHP": 50, "move": "Headbutt",
                   "atk": 5, "EXP": 10, "gold": 5, "runnable": True}
    list_of_pre_lvl_10_mobs = [mutant_boar, soldier]
    return list_of_pre_lvl_10_mobs


def make_post_lv_10_field_mobs() -> list:
    """
    Create a list of dictionaries of post-level 10 field mobs with the following keys: name, currentHP, maxHP, atk,
    move, EXP, gold, runnable.
    
    :postcondition: create a list of dictionaries of post-level 10 field mobs
    :return: a list of dictionaries of post-level 10 field mobs
    
    >>> make_post_lv_10_field_mobs()
    [{'name': 'Imp', 'currentHP': 100, 'maxHP': 100, 'atk': 15, 'EXP': 25, 'move': 'Tail Whip', 'gold': 20,
    'runnable': True}, {'name': 'Legion Commander', 'currentHP': 400, 'maxHP': 400, 'move': 'Sword Slash',
    'atk': 20, 'EXP': 60, 'gold': 75, 'runnable': True}]
    """
    imp = {"name": "Imp", "currentHP": 300, "maxHP": 300, "atk": 20, "EXP": 35,
           "move": "Tail Whip", "gold": 20, "runnable": True}
    commander = {"name": "Legion Commander", "currentHP": 400, "maxHP": 400,
                 "move": "Sword Slash", "atk": 40, "EXP": 60, "gold": 75, "runnable": True}
    list_of_post_lvl_10_mobs = [imp, commander]
    return list_of_post_lvl_10_mobs


def make_marbas() -> dict:
    """
    Create a dictionary of the boss Marbas with the following keys: name, currentHP, maxHP, atk, move, EXP, gold,
    runnable.
    
    :postcondition: create a dictionary of the boss Marbas
    :return: a dictionary of the boss Marbas
    
    >>> make_marbas()
    {'name': 'Marbas', 'currentHP': 800, 'maxHP': 800, 'atk': 40, 'EXP': 1000, 'gold': 300, 'move': 'Tainting Hands',
    'runnable': False}
    """
    boss = {"name": "Marbas", "currentHP": 800, "maxHP": 800, "atk": 65, "EXP": 1000, "gold": 300,
            "move": "Tainting Hands", "runnable": False}
    return boss


def make_andromalius() -> dict:
    """
    Create a dictionary of the boss Andromalius with the following keys: name, currentHP, maxHP, atk, move, EXP, gold,
    runnable.
    
    :postcondition: create a dictionary of the boss Andromalius
    :return: a dictionary of the boss Andromalius
    
    >>> make_andromalius()
    {'name': 'Andromalius', 'currentHP': 900, 'maxHP': 900, 'atk': 35, 'EXP': 1100, 'gold': 350,
    'move': "Serpent's Fang", 'runnable': False}
    """
    boss = {"name": "Andromalius", "currentHP": 1000, "maxHP": 1000, "atk": 55, "EXP": 1100, "gold": 350,
            "move": "Serpent's Fang", "runnable": False}
    return boss


def make_baal() -> dict:
    """
    Create a dictionary of the boss Baal with the following keys: name, currentHP, maxHP, atk, move, EXP, gold,
    runnable.
    
    :postcondition: create a dictionary of the boss Baal
    :return: a dictionary of the boss Baal
    
    >>> make_baal()
    {'name': 'Baal', 'currentHP': 2000, 'maxHP': 2000, 'atk': 50, 'EXP': 2000, 'gold': 350,
    'move': 'Thunderstorm', 'runnable': False}
    """
    boss = {"name": "Baal", "currentHP": 2000, "maxHP": 2000, "atk": 70, "EXP": 2000, "gold": 400,
            "move": "Thunderstorm", "runnable": False}
    return boss


def make_shop() -> list:
    """
    Create a list of dictionaries of items in the shop with the following keys: name, price, added_HP, added_ATK,
    move_upgrade, amount, effect.
    
    :postcondition: create a list of dictionaries of items in the shop
    :return: a list of dictionaries of items in the shop
    
    >>> make_shop()
    [{'name': 'Pill of Vitality', 'price': 50, 'added_HP': 30, 'amount': 1,
    'effect': 'Increases maxHP by 30 points'}, {'name': 'Elixer of Vigor', 'price': 65, 'added_ATK': 10,
    'move_upgrade': 'Arcane Barrage', 'amount': 1, 'effect': 'Increases ATK by 10 points'},
    {'name': 'Forbidden White Powder', 'price': 40, 'added_EXP': 100, 'amount': 2,
    'effect': 'Increases currentEXP by 100 points'}]
    """
    pill_of_vitality = {"name": "Pill of Vitality", "price": 50, "added_HP": 10,
                        "amount": 1, "effect": "Increases maxHP by 10 points"}
    elixir_of_vigor = {"name": "Elixir of Vigor", "price": 65, "added_ATK": 3,
                       "move_upgrade": "Arcane Barrage", "amount": 1,
                       "effect": "Increases ATK by 3 points"}
    forbidden_powder = {"name": "Forbidden White Powder", "price": 100, "added_EXP": 100,
                        "amount": 50, "effect": "Increases currentEXP by 100 points"}
    list_of_items = [pill_of_vitality, elixir_of_vigor, forbidden_powder]
    return list_of_items


def main():
    char = make_character()
    print(char)


if __name__ == "__main__":
    main()
