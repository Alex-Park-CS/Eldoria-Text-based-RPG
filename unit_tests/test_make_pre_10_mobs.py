from unittest import TestCase
from helper_functions.create_entity import make_pre_lv_10_field_mobs


class Test(TestCase):
    def test_make_pre_lv_10_field_mobs(self):
        expected = [{'name': 'Mutant Boar', 'currentHP': 50, 'maxHP': 50, 'atk': 5, 'move': 'Headbutt', 'EXP': 10,
                     'gold': 5, 'runnable': True}, {'name': 'Legion Soldier', 'currentHP': 100, 'maxHP': 100,
                    'atk': 10, 'move': 'Spear Thrust', 'EXP': 25, 'gold': 20, 'runnable': True}]
        actual = make_pre_lv_10_field_mobs()
        self.assertEqual(expected, actual)
