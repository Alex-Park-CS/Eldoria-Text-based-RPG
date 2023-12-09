from unittest import TestCase
from helper_functions.create_entity import make_baal


class TestMakeBaal(TestCase):
    def test_make_baal(self):
        expected = {"name": "Baal", "currentHP": 2000, "maxHP": 2000, "atk": 50, "EXP": 2000, "gold": 350,
                    "move": "Thunderstorm", "runnable": False}
        actual = make_baal()
        self.assertEqual(expected, actual)
