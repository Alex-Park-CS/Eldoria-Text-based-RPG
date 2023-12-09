from unittest import TestCase
from helper_functions.create_entity import make_andromalius


class TestMakeAndromalius(TestCase):
    def test_make_andromalius(self):
        expected = {"name": "Andromalius", "currentHP": 900, "maxHP": 900, "atk": 35, "EXP": 1100, "gold": 350,
                    "move": "Serpent's Fang", "runnable": False}
        actual = make_andromalius()
        self.assertEqual(expected, actual)
