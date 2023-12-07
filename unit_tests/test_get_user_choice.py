from unittest import TestCase
from unittest.mock import patch
from helper_functions.movement_module import get_user_choice


class MyTestCase(TestCase):
    @patch('builtins.input', side_effect=['w'])
    def test_get_user_choice_north(self, _):
        self.assertEqual('w', get_user_choice())

    @patch('builtins.input', side_effect=['a'])
    def test_get_user_choice_west(self, _):
        self.assertEqual('a', get_user_choice())

    @patch('builtins.input', side_effect=['s'])
    def test_get_user_choice_south(self, _):
        self.assertEqual('s', get_user_choice())

    @patch('builtins.input', side_effect=['d'])
    def test_get_user_choice_east(self, _):
        self.assertEqual('d', get_user_choice())

    @patch('builtins.input', side_effect=['k'])
    def test_get_user_choice_stats(self, _):
        self.assertEqual('k', get_user_choice())

    @patch('builtins.input', side_effect=['q'])
    def test_get_user_choice_quit(self, _):
        self.assertEqual('q', get_user_choice())

    @patch('builtins.input', side_effect=['h'])
    def test_get_user_choice_Value_Error(self, _):
        with self.assertRaises(ValueError):
            get_user_choice()

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_Value_Error_number(self, _):
        with self.assertRaises(ValueError):
            get_user_choice()
