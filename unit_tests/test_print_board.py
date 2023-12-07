from unittest import TestCase
from helper_functions.display_for_users import print_board
from unittest.mock import patch
import io


class TestPrintBoard(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_one_coordinate_board(self, mock_output):
        board = {(0, 0): 'X'}
        character = {"x-position": 0, "y-position": 0}
        print_board(board, character)
        actual = mock_output.getvalue()
        expected = "O\n\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_3X3_board(self, mock_output):
        board = {(0, 0): 'X', (1, 0): ' ', (2, 0): 'X',
                 (0, 1): ' ', (1, 1): ' ', (2, 1): ' ',
                 (0, 2): 'X', (1, 2): ' ', (2, 2): 'X'}
        character = {"x-position": 1, "y-position": 1}
        print_board(board, character)
        actual = mock_output.getvalue()
        expected = "X X\n O \nX X\n\n"
        self.assertEqual(expected, actual)
