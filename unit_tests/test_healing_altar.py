import io
from unittest import TestCase
from unittest.mock import patch
from helper_functions.special_events import healing_altar


class TestHealingAltar(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_healing_altar_full_hp(self, mock_output):
        character = {'x-position': 10, 'y-position': 10, 'currentHP': 10, 'maxHP': 10, 'currentEXP': 10, 'maxEXP': 50}
        healing_altar(character)
        actual = mock_output.getvalue()
        expected = ('\nYou are at the healing altar. Heal yourself to full.\n'
                    'You now have 10 / 10 HP.\n\n')
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], character['maxHP'])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_healing_altar_not_full_hp(self, mock_output):
        character = {'x-position': 10, 'y-position': 10, 'currentHP': 2, 'maxHP': 10, 'currentEXP': 10, 'maxEXP': 50}
        healing_altar(character)
        actual = mock_output.getvalue()
        expected = ('\nYou are at the healing altar. Heal yourself to full.\n'
                    'You now have 10 / 10 HP.\n\n')
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], character['maxHP'])

