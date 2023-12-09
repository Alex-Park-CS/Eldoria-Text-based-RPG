from unittest import TestCase
from helper_functions.create_entity import make_post_lv_10_field_mobs


class TestPost10(TestCase):
    def test_make_post_lv_10_field_mobs(self):
        expected = [{'name': 'Imp', 'currentHP': 100, 'maxHP': 100, 'atk': 15, 'EXP': 25, 'move': 'Tail Whip',
                     'gold': 20, 'runnable': True}, {'name': 'Legion Commander', 'currentHP': 400, 'maxHP': 400,
                    'move': 'Sword Slash', 'atk': 20, 'EXP': 60, 'gold': 75, 'runnable': True}]
        actual = make_post_lv_10_field_mobs()
        self.assertEqual(expected, actual)