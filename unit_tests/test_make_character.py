from unittest import TestCase
from helper_functions.create_entity import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        expected = {'name': 'Ysera', 'maxHP': 100, 'currentHP': 100, 'gold': 100, 'level': 1, 'maxEXP': 50,
                    'currentEXP': 0, 'atk': 5, 'move': 'Magic Missile', 'x-position': 10, 'y-position': 20, 'orb': 0}
        actual = make_character()
        self.assertEqual(expected, actual)
