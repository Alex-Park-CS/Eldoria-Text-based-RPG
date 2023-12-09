from unittest import TestCase
from unittest.mock import patch
from helper_functions.special_events import check_if_lvl_10
import io


class TestCheckLv10(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_below_level_10(self, mock_output):
        character_test = {"name": "Ysera", "level": 5, "x-position": 10, "y-position": 20}
        check_if_lvl_10(character_test)
        expected = ('\nGatekeeper: You shall not pass!!! The roads ahead are too dangerous for\n'
                    'a low level peasant like you. Come back when you hit level 10.\n'
                    'You are pushed back roughly by the gatekeeper.\n\n')
        actual = mock_output.getvalue()
        self.assertEqual(character_test["y-position"], 21)
        self.assertEqual(expected, actual)

    def test_above_level_10(self):
        character_test = {"name": "Ysera", "level": 16, "x-position": 10, "y-position": 20}
        check_if_lvl_10(character_test)
        self.assertEqual(character_test["y-position"], 20)


