import io
from unittest import TestCase
from unittest.mock import patch
from helper_functions.special_events import treasure_event


class TestTreasureEvent(TestCase):
    @patch('random.randint', return_value=1)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_event_lower_than_6_and_drink(self, mock_output, _, __):
        character = {'x-position': 10, 'y-position': 10, 'currentHP': 5, 'maxHP': 10}
        board = {(9, 9): ' ', (9, 10): ' ', (9, 11): ' ',
                 (10, 9): ' ', (10, 10): 'T', (10, 11): ' ',
                 (11, 9): ' ', (11, 10): ' ', (11, 11): ' '}
        treasure_event(character, board)
        actual = mock_output.getvalue()
        expected = ("\nCongratulations! You have found a treasure box!\n"
                    "You open the chest to find a small vial with luscious purple liquid sloshing around.\n\n"
                    "The purple liquid revitalizes you. Gain 10 maxHP!\n"
                    "Your HP: 15 / 20\n\n")
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 15)
        self.assertEqual(character['maxHP'], 20)
        self.assertEqual(board[(10, 10)], '^')

    @patch('random.randint', return_value=6)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_event_equal_6_and_drink(self, mock_output, _, __):
        character1 = {'x-position': 9, 'y-position': 10, 'currentHP': 5, 'maxHP': 10}
        board1 = {(9, 9): ' ', (9, 10): 'T', (9, 11): ' ',
                  (10, 9): ' ', (10, 10): ' ', (10, 11): ' ',
                  (11, 9): ' ', (11, 10): ' ', (11, 11): ' '}
        treasure_event(character1, board1)
        actual = mock_output.getvalue()
        expected = ("\nCongratulations! You have found a treasure box!\n"
                    "You open the chest to find a small vial with luscious purple liquid sloshing around.\n\n"
                    "The purple liquid revitalizes you. Gain 10 maxHP!\n"
                    "Your HP: 15 / 20\n\n")
        self.assertEqual(expected, actual)
        self.assertEqual(character1['currentHP'], 15)
        self.assertEqual(character1['maxHP'], 20)
        self.assertEqual(board1[(9, 10)], '^')

    @patch('random.randint', return_value=7)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_event_over_6_and_drink(self, mock_output, _, __):
        character = {'x-position': 11, 'y-position': 11, 'currentHP': 20, 'maxHP': 25}
        board = {(9, 9): ' ', (9, 10): ' ', (9, 11): ' ',
                 (10, 9): ' ', (10, 10): ' ', (10, 11): ' ',
                 (11, 9): ' ', (11, 10): ' ', (11, 11): 'T'}
        treasure_event(character, board)
        actual = mock_output.getvalue()
        expected = ("\nCongratulations! You have found a treasure box!\n"
                    "You open the chest to find a small vial with luscious purple liquid sloshing around.\n\n"
                    "Why are you drinking random shit off the ground? You deserve this. Lose 15 maxHP.\n"
                    "Your HP: 5 / 10\n\n")
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 5)
        self.assertEqual(character['maxHP'], 10)
        self.assertEqual(board[(11, 11)], '^')

    @patch('random.randint', return_value=7)
    @patch('builtins.input', side_effect=['n'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_event_not_drink(self, mock_output, _, __):
        character1 = {'x-position': 10, 'y-position': 9, 'currentHP': 20, 'maxHP': 25}
        board1 = {(9, 9): ' ', (9, 10): 'X', (9, 11): ' ',
                  (10, 9): 'T', (10, 10): ' ', (10, 11): ' ',
                  (11, 9): ' ', (11, 10): ' ', (11, 11): ' '}
        treasure_event(character1, board1)
        actual = mock_output.getvalue()
        expected = ("\nCongratulations! You have found a treasure box!\n"
                    "You open the chest to find a small vial with luscious purple liquid sloshing around.\n\n"
                    "You decide to not drink the unknown liquid and throw the vial onto the ground.\n"
                    "Mom did always say to not eat anything you find in the streets...\n\n")
        self.assertEqual(expected, actual)
        self.assertEqual(character1['currentHP'], 20)
        self.assertEqual(character1['maxHP'], 25)
        self.assertEqual(board1[(10, 9)], '^')

    @patch('random.randint', return_value=7)
    @patch('builtins.input', side_effect=['f', 'n'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_incorrect_input(self, mock_output, _, __):
        character1 = {'x-position': 11, 'y-position': 9, 'currentHP': 20, 'maxHP': 25}
        board1 = {(9, 9): 'X', (9, 10): 'X', (9, 11): ' ',
                  (10, 9): ' ', (10, 10): ' ', (10, 11): ' ',
                  (11, 9): 'T', (11, 10): ' ', (11, 11): ' '}
        treasure_event(character1, board1)
        actual = mock_output.getvalue()
        expected = ("\nCongratulations! You have found a treasure box!\n"
                    "You open the chest to find a small vial with luscious purple liquid sloshing around.\n\n"
                    "\nInvalid input. Please enter either 'y' or 'n'.\n\n"
                    "You decide to not drink the unknown liquid and throw the vial onto the ground.\n"
                    "Mom did always say to not eat anything you find in the streets...\n\n")
        self.assertEqual(expected, actual)
        self.assertEqual(character1['currentHP'], 20)
        self.assertEqual(character1['maxHP'], 25)
        self.assertEqual(board1[(11, 9)], '^')