from unittest import TestCase
from unittest.mock import patch
from helper_functions.special_events import chance_of_event


class TestChanceOfEvent(TestCase):

    @patch('random.uniform', return_value=0.12)
    def test_chance_of_event_lower_than_param(self, _):
        expected = True
        actual = chance_of_event(0.3)
        self.assertEqual(expected, actual)

    @patch('random.uniform', return_value=0.54)
    def test_chance_of_event_higher_than_param(self, _):
        expected = False
        actual = chance_of_event(0.3)
        self.assertEqual(expected, actual)

    @patch('random.uniform', return_value=0.3)
    def test_chance_of_event_equal_param(self, _):
        expected = True
        actual = chance_of_event(0.3)
        self.assertEqual(expected, actual)

    @patch('random.uniform', return_value=0.001)
    def test_chance_of_event_zero_param(self, _):
        expected = False
        actual = chance_of_event(0)
        self.assertEqual(expected, actual)



