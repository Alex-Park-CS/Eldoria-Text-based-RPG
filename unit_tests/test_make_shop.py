from unittest import TestCase
from helper_functions.create_entity import make_shop


class TestMakeShop(TestCase):
    def test_make_shop(self):
        elixir = {"name": "Elixir of Vigor", "price": 65, "added_ATK": 3,
                  "move_upgrade": "Arcane Barrage", "amount": 1,
                  "effect": "Increases ATK by 3 points"}
        powder = {"name": "Forbidden White Powder", "price": 100, "added_EXP": 100,
                  "amount": 50, "effect": "Increases currentEXP by 100 points"}
        pill = {"name": "Pill of Vitality", "price": 50, "added_HP": 10,
                "amount": 1, "effect": "Increases maxHP by 10 points"}
        expected = [pill, elixir, powder]
        actual = make_shop()
        self.assertEqual(expected, actual)
