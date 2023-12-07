from unittest import TestCase
from helper_functions.movement_module import move_character


class TestMoveCharacter(TestCase):

    def test_move_north(self):
        test_character = {'x-position': 5, 'y-position': 5, 'HP': 5}
        expected = {'x-position': 5, 'y-position': 4, 'HP': 5}
        move_character(test_character, 'w')
        self.assertEqual(expected, test_character)

    def test_move_west(self):
        test_character = {'x-position': 5, 'y-position': 5, 'HP': 5}
        expected = {'x-position': 4, 'y-position': 5, 'HP': 5}
        move_character(test_character, 'a')
        self.assertEqual(expected, test_character)

    def test_move_south(self):
        test_character = {'x-position': 5, 'y-position': 5, 'HP': 5}
        expected = {'x-position': 5, 'y-position': 6, 'HP': 5}
        move_character(test_character, 's')
        self.assertEqual(expected, test_character)

    def test_move_east(self):
        test_character = {'x-position': 5, 'y-position': 5, 'HP': 5}
        expected = {'x-position': 6, 'y-position': 5, 'HP': 5}
        move_character(test_character, 'd')
        self.assertEqual(expected, test_character)
