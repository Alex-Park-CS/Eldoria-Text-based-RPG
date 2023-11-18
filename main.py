# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def make_board(rows, columns):
    """
    Create a game board using the rows and columns parameters.

    A text-base game board requires a number of rows and columns to create a virtual board where the players can
    move through. Each coordinate is denoted such as: (0,1), indicating the x position with the first number, and the
    y position with the second number. Each room has a description of one of "Empty room", "Ominous Hallway",
    "Room of Skulls", "Altar of Magic", which describe the type of room the player is in.

    :param rows: positive, non-zero integer
    :param columns: another positive, non-zero integer
    :precondition rows: must be an integer greater than or equal to 2
    :precondition columns: must be also an integer greater than or equal to 2
    :postcondition: create a game board which has the number of rows and columns as given in the parameters; each
    coordinate has a room description
    :return: a dictionary with tuples as the keys, and strings as values

    """
    map_of_board= \
        ("|xxxxxxxxxx xxxxxxxxxx|"
         "|xxxxxxxxxx xxxxxxxxxx|"
         "|xxxxxxxxxx xxxxxxxxxx|"
         "|xxxxxxxxxx xxxxxxxxxx|"
         "|xxxxxxxxxx xxxxxxxxxx|"
         "|xxxxxxxxxx xxxxxxxxxx|"
         "|xxxxxxxxxx xxxxxxxxxx|"
         "|xxxxxxxxxx xxxxxxxxxx|"
         "|xxxxxxxxxxxxxxxxxxxxx|")


    choice_of_rooms = ("Empty Room", "Room of Skulls", "Alter of Magic", "Ominous Hallway")
    board_dict = {(x_position, y_position): choice_of_rooms[random.randint(0, 3)]
                  for x_position in range(rows) for y_position in range(columns)}
    return board_dict


def main():
    var = make_board(2, 2)
    print(var)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
