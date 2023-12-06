import time


def describe_current_location(board, character):
    """
    Shows the current location of the character.

    Using the x-position and y-position keys of the character variable, shows the user the current location of the
    player, and what type of room they are in (i.e. Empty Room)

    :param board: a dictionary
    :param character: another dictionary
    :precondition board: a non-empty game board that has been created
    :precondition character: a dictionary with x and y positions that are equal or greater than 0
    :postcondition: shows user the current location of the character and the name of the type of room they are in
    :return: a dictionary
    """
    current_position = (character["x-position"], character["y-position"])
    return board[current_position]


def print_board(board, character):

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
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Add a newline at the end






