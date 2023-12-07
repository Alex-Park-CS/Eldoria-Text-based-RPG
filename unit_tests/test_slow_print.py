from unittest import TestCase
from helper_functions.display_for_users import slow_print
from unittest.mock import patch
import io


class TestSlowPrint(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_slow_print_base(self, mock_output):
        text = "asdf asdf asdf jkl;"
        slow_print(text)
        actual = mock_output.getvalue()
        expected = "asdf asdf asdf jkl;\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_slow_print_delay(self, mock_output):
        text = "Every character is delayed by 0.1 seconds."
        slow_print(text, 0.1)
        actual = mock_output.getvalue()
        expected = "Every character is delayed by 0.1 seconds.\n"
        self.assertEqual(expected, actual)
