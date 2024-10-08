from unittest import TestCase
from helper_functions.create_entity import make_board


class TestMakeBoard(TestCase):
    def test_make_board(self):
        expected =  {(0, 0): 'X',
                     (0, 1): 'X',
                     (0, 2): 'X',
                     (0, 3): 'X',
                     (0, 4): 'X',
                     (0, 5): 'X',
                     (0, 6): 'X',
                     (0, 7): 'X',
                     (0, 8): 'X',
                     (0, 9): 'X',
                     (0, 10): 'X',
                     (0, 11): 'X',
                     (0, 12): 'X',
                     (0, 13): 'X',
                     (0, 14): 'X',
                     (0, 15): 'X',
                     (0, 16): 'X',
                     (0, 17): 'X',
                     (0, 18): 'X',
                     (0, 19): 'X',
                     (0, 20): 'X',
                     (1, 0): 'X',
                     (1, 1): 'X',
                     (1, 2): '*',
                     (1, 3): '*',
                     (1, 4): '*',
                     (1, 5): '*',
                     (1, 6): '*',
                     (1, 7): ' ',
                     (1, 8): '*',
                     (1, 9): 'X',
                     (1, 10): 'X',
                     (1, 11): 'H',
                     (1, 12): ' ',
                     (1, 13): '^',
                     (1, 14): ' ',
                     (1, 15): '^',
                     (1, 16): ' ',
                     (1, 17): ' ',
                     (1, 18): '^',
                     (1, 19): ' ',
                     (1, 20): 'X',
                     (2, 0): 'X',
                     (2, 1): 'X',
                     (2, 2): '*',
                     (2, 3): '*',
                     (2, 4): '*',
                     (2, 5): '*',
                     (2, 6): '*',
                     (2, 7): ' ',
                     (2, 8): '*',
                     (2, 9): 'X',
                     (2, 10): 'X',
                     (2, 11): ' ',
                     (2, 12): ' ',
                     (2, 13): '^',
                     (2, 14): '^',
                     (2, 15): 'X',
                     (2, 16): '^',
                     (2, 17): '^',
                     (2, 18): ' ',
                     (2, 19): ' ',
                     (2, 20): 'X',
                     (3, 0): 'X',
                     (3, 1): 'X',
                     (3, 2): '*',
                     (3, 3): '*',
                     (3, 4): '*',
                     (3, 5): '*',
                     (3, 6): '*',
                     (3, 7): ' ',
                     (3, 8): '*',
                     (3, 9): 'X',
                     (3, 10): 'X',
                     (3, 11): ' ',
                     (3, 12): ' ',
                     (3, 13): 'X',
                     (3, 14): '^',
                     (3, 15): 'X',
                     (3, 16): '^',
                     (3, 17): '^',
                     (3, 18): ' ',
                     (3, 19): '^',
                     (3, 20): 'X',
                     (4, 0): 'X',
                     (4, 1): 'X',
                     (4, 2): '*',
                     (4, 3): '*',
                     (4, 4): '*',
                     (4, 5): '*',
                     (4, 6): 'X',
                     (4, 7): ' ',
                     (4, 8): '*',
                     (4, 9): 'X',
                     (4, 10): 'X',
                     (4, 11): ' ',
                     (4, 12): '^',
                     (4, 13): '^',
                     (4, 14): '^',
                     (4, 15): 'X',
                     (4, 16): '^',
                     (4, 17): '^',
                     (4, 18): '^',
                     (4, 19): ' ',
                     (4, 20): 'X',
                     (5, 0): 'X',
                     (5, 1): 'X',
                     (5, 2): '*',
                     (5, 3): '*',
                     (5, 4): '*',
                     (5, 5): 'X',
                     (5, 6): 'X',
                     (5, 7): ' ',
                     (5, 8): '*',
                     (5, 9): 'X',
                     (5, 10): 'X',
                     (5, 11): '^',
                     (5, 12): ' ',
                     (5, 13): '^',
                     (5, 14): '^',
                     (5, 15): 'T',
                     (5, 16): 'X',
                     (5, 17): '^',
                     (5, 18): ' ',
                     (5, 19): ' ',
                     (5, 20): 'X',
                     (6, 0): 'X',
                     (6, 1): 'X',
                     (6, 2): 'A',
                     (6, 3): '*',
                     (6, 4): 'X',
                     (6, 5): ' ',
                     (6, 6): 'X',
                     (6, 7): ' ',
                     (6, 8): '*',
                     (6, 9): 'X',
                     (6, 10): 'X',
                     (6, 11): ' ',
                     (6, 12): '^',
                     (6, 13): 'X',
                     (6, 14): '^',
                     (6, 15): 'X',
                     (6, 16): 'X',
                     (6, 17): '^',
                     (6, 18): '^',
                     (6, 19): '^',
                     (6, 20): 'X',
                     (7, 0): 'X',
                     (7, 1): 'X',
                     (7, 2): 'X',
                     (7, 3): 'X',
                     (7, 4): ' ',
                     (7, 5): ' ',
                     (7, 6): 'X',
                     (7, 7): ' ',
                     (7, 8): '*',
                     (7, 9): 'X',
                     (7, 10): 'X',
                     (7, 11): ' ',
                     (7, 12): ' ',
                     (7, 13): '^',
                     (7, 14): '^',
                     (7, 15): 'X',
                     (7, 16): '^',
                     (7, 17): '^',
                     (7, 18): ' ',
                     (7, 19): ' ',
                     (7, 20): 'X',
                     (8, 0): 'X',
                     (8, 1): 'X',
                     (8, 2): 'X',
                     (8, 3): ' ',
                     (8, 4): ' ',
                     (8, 5): ' ',
                     (8, 6): 'X',
                     (8, 7): ' ',
                     (8, 8): '*',
                     (8, 9): 'X',
                     (8, 10): 'X',
                     (8, 11): ' ',
                     (8, 12): ' ',
                     (8, 13): ' ',
                     (8, 14): ' ',
                     (8, 15): ' ',
                     (8, 16): ' ',
                     (8, 17): ' ',
                     (8, 18): ' ',
                     (8, 19): ' ',
                     (8, 20): 'X',
                     (9, 0): 'X',
                     (9, 1): 'X',
                     (9, 2): ' ',
                     (9, 3): ' ',
                     (9, 4): ' ',
                     (9, 5): ' ',
                     (9, 6): 'X',
                     (9, 7): ' ',
                     (9, 8): '*',
                     (9, 9): 'X',
                     (9, 10): 'X',
                     (9, 11): 'S',
                     (9, 12): ' ',
                     (9, 13): ' ',
                     (9, 14): ' ',
                     (9, 15): ' ',
                     (9, 16): ' ',
                     (9, 17): ' ',
                     (9, 18): ' ',
                     (9, 19): ' ',
                     (9, 20): ' ',
                     (10, 0): 'X',
                     (10, 1): 'X',
                     (10, 2): 'B',
                     (10, 3): ' ',
                     (10, 4): ' ',
                     (10, 5): ' ',
                     (10, 6): '-',
                     (10, 7): ' ',
                     (10, 8): ' ',
                     (10, 9): ' ',
                     (10, 10): '/',
                     (10, 11): ' ',
                     (10, 12): ' ',
                     (10, 13): ' ',
                     (10, 14): ' ',
                     (10, 15): ' ',
                     (10, 16): ' ',
                     (10, 17): ' ',
                     (10, 18): ' ',
                     (10, 19): ' ',
                     (10, 20): ' ',
                     (11, 0): 'X',
                     (11, 1): 'X',
                     (11, 2): ' ',
                     (11, 3): ' ',
                     (11, 4): ' ',
                     (11, 5): ' ',
                     (11, 6): 'X',
                     (11, 7): ' ',
                     (11, 8): '*',
                     (11, 9): 'X',
                     (11, 10): 'X',
                     (11, 11): ' ',
                     (11, 12): ' ',
                     (11, 13): ' ',
                     (11, 14): ' ',
                     (11, 15): ' ',
                     (11, 16): ' ',
                     (11, 17): ' ',
                     (11, 18): ' ',
                     (11, 19): ' ',
                     (11, 20): ' ',
                     (12, 0): 'X',
                     (12, 1): 'X',
                     (12, 2): 'X',
                     (12, 3): ' ',
                     (12, 4): ' ',
                     (12, 5): ' ',
                     (12, 6): 'X',
                     (12, 7): ' ',
                     (12, 8): '*',
                     (12, 9): 'X',
                     (12, 10): 'X',
                     (12, 11): ' ',
                     (12, 12): ' ',
                     (12, 13): '^',
                     (12, 14): ' ',
                     (12, 15): '^',
                     (12, 16): ' ',
                     (12, 17): ' ',
                     (12, 18): ' ',
                     (12, 19): ' ',
                     (12, 20): 'X',
                     (13, 0): 'X',
                     (13, 1): 'X',
                     (13, 2): 'X',
                     (13, 3): 'X',
                     (13, 4): ' ',
                     (13, 5): ' ',
                     (13, 6): 'X',
                     (13, 7): ' ',
                     (13, 8): '*',
                     (13, 9): 'X',
                     (13, 10): 'X',
                     (13, 11): ' ',
                     (13, 12): ' ',
                     (13, 13): ' ',
                     (13, 14): ' ',
                     (13, 15): 'X',
                     (13, 16): 'X',
                     (13, 17): '^',
                     (13, 18): ' ',
                     (13, 19): ' ',
                     (13, 20): 'X',
                     (14, 0): 'X',
                     (14, 1): 'X',
                     (14, 2): 'M',
                     (14, 3): '*',
                     (14, 4): 'X',
                     (14, 5): ' ',
                     (14, 6): 'X',
                     (14, 7): ' ',
                     (14, 8): '*',
                     (14, 9): 'X',
                     (14, 10): 'X',
                     (14, 11): ' ',
                     (14, 12): ' ',
                     (14, 13): '^',
                     (14, 14): ' ',
                     (14, 15): '^',
                     (14, 16): 'X',
                     (14, 17): ' ',
                     (14, 18): ' ',
                     (14, 19): ' ',
                     (14, 20): 'X',
                     (15, 0): 'X',
                     (15, 1): 'X',
                     (15, 2): '*',
                     (15, 3): '*',
                     (15, 4): '*',
                     (15, 5): 'X',
                     (15, 6): 'X',
                     (15, 7): ' ',
                     (15, 8): '*',
                     (15, 9): 'X',
                     (15, 10): 'X',
                     (15, 11): ' ',
                     (15, 12): ' ',
                     (15, 13): ' ',
                     (15, 14): 'X',
                     (15, 15): 'X',
                     (15, 16): 'X',
                     (15, 17): ' ',
                     (15, 18): ' ',
                     (15, 19): ' ',
                     (15, 20): 'X',
                     (16, 0): 'X',
                     (16, 1): 'X',
                     (16, 2): '*',
                     (16, 3): '*',
                     (16, 4): '*',
                     (16, 5): '*',
                     (16, 6): 'X',
                     (16, 7): ' ',
                     (16, 8): '*',
                     (16, 9): 'X',
                     (16, 10): 'X',
                     (16, 11): ' ',
                     (16, 12): 'X',
                     (16, 13): ' ',
                     (16, 14): 'X',
                     (16, 15): 'T',
                     (16, 16): 'X',
                     (16, 17): ' ',
                     (16, 18): ' ',
                     (16, 19): ' ',
                     (16, 20): 'X',
                     (17, 0): 'X',
                     (17, 1): 'X',
                     (17, 2): '*',
                     (17, 3): '*',
                     (17, 4): '*',
                     (17, 5): '*',
                     (17, 6): '*',
                     (17, 7): ' ',
                     (17, 8): '*',
                     (17, 9): 'X',
                     (17, 10): 'X',
                     (17, 11): ' ',
                     (17, 12): '^',
                     (17, 13): '^',
                     (17, 14): 'X',
                     (17, 15): '^',
                     (17, 16): 'X',
                     (17, 17): ' ',
                     (17, 18): ' ',
                     (17, 19): ' ',
                     (17, 20): 'X',
                     (18, 0): 'X',
                     (18, 1): 'X',
                     (18, 2): '*',
                     (18, 3): '*',
                     (18, 4): '*',
                     (18, 5): '*',
                     (18, 6): '*',
                     (18, 7): ' ',
                     (18, 8): '*',
                     (18, 9): 'X',
                     (18, 10): 'X',
                     (18, 11): ' ',
                     (18, 12): 'X',
                     (18, 13): 'X',
                     (18, 14): 'X',
                     (18, 15): ' ',
                     (18, 16): 'X',
                     (18, 17): ' ',
                     (18, 18): '^',
                     (18, 19): ' ',
                     (18, 20): 'X',
                     (19, 0): 'X',
                     (19, 1): 'X',
                     (19, 2): '*',
                     (19, 3): '*',
                     (19, 4): '*',
                     (19, 5): '*',
                     (19, 6): '*',
                     (19, 7): ' ',
                     (19, 8): 'H',
                     (19, 9): 'X',
                     (19, 10): 'X',
                     (19, 11): 'H',
                     (19, 12): ' ',
                     (19, 13): '^',
                     (19, 14): ' ',
                     (19, 15): ' ',
                     (19, 16): 'X',
                     (19, 17): ' ',
                     (19, 18): ' ',
                     (19, 19): ' ',
                     (19, 20): 'X',
                     (20, 0): 'X',
                     (20, 1): 'X',
                     (20, 2): 'X',
                     (20, 3): 'X',
                     (20, 4): 'X',
                     (20, 5): 'X',
                     (20, 6): 'X',
                     (20, 7): 'X',
                     (20, 8): 'X',
                     (20, 9): 'X',
                     (20, 10): 'X',
                     (20, 11): 'X',
                     (20, 12): 'X',
                     (20, 13): 'X',
                     (20, 14): 'X',
                     (20, 15): 'X',
                     (20, 16): 'X',
                     (20, 17): 'X',
                     (20, 18): 'X',
                     (20, 19): 'X',
                     (20, 20): 'X'}
        actual = make_board()
        self.assertEqual(expected, actual)
