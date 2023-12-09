from unittest import TestCase
from unittest.mock import patch
from helper_functions.special_events import check_for_orbs
import io


class TestCheckOrbs(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_orbs_below_2(self, mock_output):
        character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                          "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                          "x-position": 10, "y-position": 20, "orb": 0}
        check_for_orbs(character_test)
        actual = mock_output.getvalue()
        expected = ("\nThe two massive doors are sealed shut, and you see two divots in the shape of a sphere.\n"
                    "You are pushed back roughly by an unknown force.\n\n")
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_orbs_equal_2(self, mock_output):
        character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                          "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                          "x-position": 10, "y-position": 20, "orb": 2}
        check_for_orbs(character_test)
        actual = mock_output.getvalue()
        expected = ("The two orbs in your inventory fly out and fit right into the divots of the door.\n"
                    "The door slowly creaks open, to uncover a long corridor...\n\n")
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_orbs_above_2(self, mock_output):
        character_test = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                          "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                          "x-position": 10, "y-position": 20, "orb": 6}
        check_for_orbs(character_test)
        actual = mock_output.getvalue()
        expected = ("The two orbs in your inventory fly out and fit right into the divots of the door.\n"
                    "The door slowly creaks open, to uncover a long corridor...\n\n")
        self.assertEqual(expected, actual)
