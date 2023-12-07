from unittest import TestCase
from helper_functions.movement_module import validate_move


class TestValidMove(TestCase):
    def test_validate_move_north(self):
        character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                          "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                          "x-position": 1, "y-position": 2, "orb": 0}
        board_test = {(0, 0): 'X', (0, 1): 'X', (0, 2): ' ', (0, 3): 'X',
                      (1, 0): ' ', (1, 1): 'X', (1, 2): ' ', (1, 3): 'X',
                      (2, 0): 'X', (2, 1): 'X', (2, 2): ' ', (2, 3): 'X', }
        direction_test = 'w'
        expected = False
        actual = validate_move(board_test, character_test, direction_test)
        self.assertEqual(expected, actual)

    def test_validate_move_west(self):
        character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 2,
                          "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                          "x-position": 1, "y-position": 2, "orb": 0}
        board_test = {(0, 0): 'X', (0, 1): ' ', (0, 2): ' ', (0, 3): 'X',
                      (1, 0): ' ', (1, 1): 'X', (1, 2): ' ', (1, 3): 'X',
                      (2, 0): 'X', (2, 1): 'X', (2, 2): ' ', (2, 3): 'X', }
        direction_test = 'a'
        expected = True
        actual = validate_move(board_test, character_test, direction_test)
        self.assertEqual(expected, actual)

    def test_validate_move_south(self):
        character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 3,
                          "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                          "x-position": 1, "y-position": 2, "orb": 0}
        board_test = {(0, 0): 'X', (0, 1): ' ', (0, 2): ' ', (0, 3): '*',
                      (1, 0): ' ', (1, 1): 'X', (1, 2): ' ', (1, 3): 'X',
                      (2, 0): 'X', (2, 1): 'X', (2, 2): ' ', (2, 3): 'X', }
        direction_test = 's'
        expected = False
        actual = validate_move(board_test, character_test, direction_test)
        self.assertEqual(expected, actual)

    def test_validate_move_east(self):
        character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 2,
                          "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                          "x-position": 1, "y-position": 2, "orb": 0}
        board_test = {(0, 0): 'X', (0, 1): ' ', (0, 2): ' ', (0, 3): 'X',
                      (1, 0): ' ', (1, 1): 'X', (1, 2): 'X', (1, 3): 'X',
                      (2, 0): 'X', (2, 1): 'X', (2, 2): ' ', (2, 3): 'X', }
        direction_test = 'd'
        expected = True
        actual = validate_move(board_test, character_test, direction_test)
        self.assertEqual(expected, actual)

    def test_validate_move_stats(self):
        character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                          "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                          "x-position": 1, "y-position": 2, "orb": 0}
        board_test = {(0, 0): 'X', (0, 1): ' ', (0, 2): ' ', (0, 3): ' ',
                      (1, 0): ' ', (1, 1): 'X', (1, 2): 'X', (1, 3): 'X',
                      (2, 0): 'X', (2, 1): 'X', (2, 2): ' ', (2, 3): 'X', }
        direction_test = 'k'
        expected = False
        actual = validate_move(board_test, character_test, direction_test)
        self.assertEqual(expected, actual)

    def test_validate_move_not_a_command(self):
        character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 5,
                          "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                          "x-position": 1, "y-position": 2, "orb": 0}
        board_test = {(0, 0): 'X', (0, 1): ' ', (0, 2): ' ', (0, 3): '^',
                      (1, 0): ' ', (1, 1): 'X', (1, 2): 'X', (1, 3): 'X',
                      (2, 0): 'X', (2, 1): 'X', (2, 2): ' ', (2, 3): 'X', }
        direction_test = 'kj'
        expected = False
        actual = validate_move(board_test, character_test, direction_test)
        self.assertEqual(expected, actual)
