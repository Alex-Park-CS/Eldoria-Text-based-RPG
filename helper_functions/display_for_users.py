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
