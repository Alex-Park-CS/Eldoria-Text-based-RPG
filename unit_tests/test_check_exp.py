import io
from unittest import TestCase
from unittest.mock import patch
from helper_functions.special_events import check_exp


class TestExp(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_exp_current_less_than_max(self, mock_output):
        character = {'x-position': 10, 'y-position': 10, 'currentHP': 5, 'maxHP': 10, 'currentEXP': 10, 'maxEXP': 50}
        check_exp(character)
        actual = mock_output.getvalue()
        expected = ''
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_exp_current_more_than_max(self, mock_output):
        character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                          "maxEXP": 50, "currentEXP": 65, "atk": 5, "move": "Magic Missile",
                          "x-position": 10, "y-position": 20, "orb": 0}
        check_exp(character_test)
        actual = mock_output.getvalue()
        exp = ('\nYou have leveled up! You are now level 2. You feel stronger, as the aura around you settles down.\n'
               'Your new stats --- HP: 110 / 110 --- ATK: 6 --- EXP: 15 / 55\n\n')
        self.assertEqual(exp, actual)
        self.assertEqual(character_test['currentHP'], 110)
        self.assertEqual(character_test['maxHP'], 110)
        self.assertEqual(character_test['atk'], 6)
        self.assertEqual(character_test['currentEXP'], 15)
        self.assertEqual(character_test['maxEXP'], 55)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_exp_more_than_1_lvl_up(self, mock_output):
        character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                          "maxEXP": 50, "currentEXP": 110, "atk": 5, "move": "Magic Missile",
                          "x-position": 10, "y-position": 20, "orb": 0}
        check_exp(character_test)
        actual = mock_output.getvalue()
        exp = ('\nYou have leveled up! You are now level 2. You feel stronger, as the aura around you settles down.\n'
               'Your new stats --- HP: 110 / 110 --- ATK: 6 --- EXP: 60 / 55\n\n'
               '\nYou have leveled up! You are now level 3. You feel stronger, as the aura around you settles down.\n'
               'Your new stats --- HP: 121 / 121 --- ATK: 7 --- EXP: 5 / 60\n\n')
        self.assertEqual(exp, actual)
        self.assertEqual(character_test['currentHP'], 121)
        self.assertEqual(character_test['maxHP'], 121)
        self.assertEqual(character_test['atk'], 7)
        self.assertEqual(character_test['currentEXP'], 5)
        self.assertEqual(character_test['maxEXP'], 60)
