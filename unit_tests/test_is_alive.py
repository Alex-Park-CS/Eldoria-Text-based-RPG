import unittest
from helper_functions.character_module import is_alive


class TestAlive(unittest.TestCase):
    def test_is_alive(self):
        character = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                     "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        self.assertEqual(True, is_alive(character))

    def test_is_HP_0(self):
        character = {"name": "Ysera", "maxHP": 100, "currentHP": 0, "gold": 100, "level": 1,
                     "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        self.assertEqual(False, is_alive(character))

    def test_is_HP_less_than_0(self):
        character = {"name": "Ysera", "maxHP": 100, "currentHP": -30, "gold": 100, "level": 1,
                     "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        self.assertEqual(False, is_alive(character))
