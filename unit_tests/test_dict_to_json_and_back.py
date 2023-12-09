from unittest import TestCase
from helper_functions.save_module import dict_to_json_string_conversion


class TestDictJson(TestCase):
    def test_dict_to_json_string_conversion_json_to_tuple(self):
        expected = {'(1, 2)': 'X', '(3, 4)': 'O'}
        test_dict = {(1, 2): 'X', (3, 4): 'O'}
        actual = dict_to_json_string_conversion(test_dict)
        self.assertEqual(expected, actual)

    def test_dict_to_json_string_conversion_tuple_to_json(self):
        expected = {(1, 2): 'X', (3, 4): 'O'}
        test_dict = {'(1, 2)': 'X', '(3, 4)': 'O'}
        actual = dict_to_json_string_conversion(test_dict)
        self.assertEqual(expected, actual)
