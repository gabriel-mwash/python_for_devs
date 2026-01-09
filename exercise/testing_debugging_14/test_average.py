import unittest
from average_with_none_values import average


class TestAverage(unittest.TestCase):
    """ tests for average """

    def test_for_empty(self):
        """ test for empty list """
        expected = "empty list"
        result = average([])
        self.assertEqual(expected, result,
                        " the list is empty")

    def test_for_one_item(self):
        expected = 13
        result = average([13])
        self.assertEqual(expected, result,
                         "the list has one item")

    def test_for_list_with_empty(self):
        expected = 25.0
        result = average([20, None, 30])
        self.assertEqual(expected, result,
                         " the list has a empty value")

    def test_for_nonempty(self):
        expected = 20.0
        result = average([10, 30, 50, 5, 5])
        self.assertEqual(expected, result,
                         "the list is non empty")

unittest.main()
