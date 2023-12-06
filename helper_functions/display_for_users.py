import time


def print_board(board, character):
    """
    Print the minimap of the game board.
    
    :param board: a dictionary
    :param character: a dictionary
    :precondition board: a dictionary that represents the game board
    :precondition character: a dictionary that represents the character
    :postcondition: print the minimap of the game board

    >>> board = {(0, 0): 'X', (0, 1): ' ', (0, 2): 'X',
                 (1, 0): 'X', (1, 1): 'X', (1, 2): 'X',
                 (2, 0): 'X', (2, 1): ' ', (2, 2): 'X'}
    >>> character = {'x-position': 1, 'y-position': 1}
    >>> print_board(board, character)
    X X
    XOX
    X X
    """

    for col in range(21):
        for row in range(21):
            if (character["x-position"], character["y-position"]) == (row, col):
                print("O", end='')
            else:
                print(board[row, col], end='')
        print()


def intro_prompt():
    prompt = (
        "E   L   D   O   R   I   A\n\n"

        "Venture forth, intrepid mage Ysera, into the depths of Eldoria's mystical dungeons! \n"
        "The air is thick with ancient enchantments and the ominous echoes of your adversaries—Demon Lord Baal,\n"
        "and his nefarious subordinates Marbas, and Andromalius. As a formidable mage, your attacks are not just\n"
        "spells but a blend of arcane mastery and the unpredictability of dice rolls.\n\n"

        "Equipped with your trusty staff, each swing and incantation is influenced by the fickle hand of fate.\n"
        "Your base attack forms the foundation of your magical might, but the outcome is determined by the \n"
        "roll of the dice.\n\n"

        "The lands teem with malevolent creatures and cunning traps. Face off against mutations, soldiers that \n"
        "have pledged their lives for the horde and disgusting demons, all while calculating the potency of your \n"
        "attacks. Harness your arcane knowledge to decipher the weaknesses of your foes and enhance the power \n"
        "of your strikes.\n\n"

        "In the heart of darkness, Demon Lord Baal awaits, guarded by Marbas and Andromalius. As you confront \n"
        "these formidable adversaries, unleash your magical prowess and let the dice decide the fate of your \n"
        "spells. A mighty barrage of magic or a subtle charm—all outcomes are determined by the roll of the dice. \n"
        "Prepare to navigate the intricate dance between strategy and chance, noble mage. Eldoria's destiny rests \n"
        "upon your magical prowess and the whims of the dice. Will you emerge victorious, casting aside the shadows \n"
        "that threaten to engulf the realm? The dungeons beckon, and your journey unfolds with every roll of the \n"
        "dice. May your spells be potent, and your rolls be in your favor!\n"
    )
    return prompt


def slow_print(text, delay=0.007):
    """
    Print one character at a time with a delay between each character.
    
    :param text: a string
    :param delay: a float
    :precondition text: a string
    :precondition delay: a float
    :postcondition: print one character at a time with a delay between each character
    
    >>> slow_print("Hello, World!")
    Hello, World!
    
    >>> slow_print("Hello, World!", 0.1)
    Hello, World!
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Add a newline at the end


def print_character_stats(character):
    """
    Print the character's stats.
    
    :param character: a dictionary
    :precondition character: a dictionary that represents the character
    :postcondition: print the character's stats
    
    >>> character = {'level': 1, 'maxHP': 10, 'currentHP': 10, 'atk': 1, 'gold': 0, 'currentEXP': 0, 'maxEXP': 10}
    >>> print_character_stats(character)
    ------Current Stats------
    Your Level: 1
    Your HP: 10 / 10
    Your ATK: 1
    Your gold: 0
    Your EXP: 0 / 10 XP.
    """
    slow_print(f"\n------Current Stats------\n"
               f"Your Level: {character['level']}\n"
               f"Your HP: {character['currentHP']} / {character['maxHP']}\n"
               f"Your ATK: {character['atk']}\n"
               f"Your gold: {character['gold']}\n"
               f"Your EXP: {character['currentEXP']} / {character['maxEXP']} XP.\n")




