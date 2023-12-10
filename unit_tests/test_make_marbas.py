from unittest import TestCase
from helper_functions.create_entity import make_marbas


class TestMakeMarbas(TestCase):
    def test_make_marbas(self):
        expected = {"name": "Marbas", "currentHP": 800, "maxHP": 800, "atk": 65, "EXP": 1000, "gold": 300,
                    "move": "Tainting Hands", "runnable": False}
        actual = make_marbas()
        self.assertEqual(expected, actual)
