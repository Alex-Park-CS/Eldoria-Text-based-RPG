from unittest import TestCase
from helper_functions.display_for_users import print_character_stats
from unittest.mock import patch
import io


class TestCharStats(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_base_char_stats(self, mock_output):
        character = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                     "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        print_character_stats(character)
        actual = mock_output.getvalue()
        expected = ("\n------Current Stats------\n"
                    "Your Level: 1\n"
                    "Your HP: 100 / 100\n"
                    "Your ATK: 5\n"
                    "Your gold: 100\n"
                    "Your EXP: 0 / 50 XP.\n\n")
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_post_mid_boss_char_stats(self, mock_output):
        character = {"name": "Ysera", "maxHP": 700, "currentHP": 420, "gold": 2100, "level": 15,
                     "maxEXP": 612, "currentEXP": 147, "atk": 35, "move": "Arcane Barrage",
                     "x-position": 10, "y-position": 20, "orb": 1}
        print_character_stats(character)
        actual = mock_output.getvalue()
        expected = ("\n------Current Stats------\n"
                    "Your Level: 15\n"
                    "Your HP: 420 / 700\n"
                    "Your ATK: 35\n"
                    "Your gold: 2100\n"
                    "Your EXP: 147 / 612 XP.\n\n")
        self.assertEqual(expected, actual)
