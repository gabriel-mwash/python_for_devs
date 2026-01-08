import unittest
from sort import is_sorted



class TestSorted(unittest.TestCase):
    """ tests for is_sorted """

    def test_empty_list(self):
        expected = []
        result = is_sorted([])
        self.assertEqual(expected, result,
                         " empty list")

    def test_one_element_list(self):
        expected = [1]
        result = is_sorted([1])
        self.assertEqual(expected, result,
                         "one element list")

    def test_not_sorted_list(self):
        expected = False
        result = is_sorted([4, 2, 1])
        self.assertEqual(expected, result,
                         " not sorted")

    def test_not_sorted_long_list(self):
        expected = False
        result = is_sorted([1, 2, 3, 4, 7, 8, 7])
        self.assertEqual(expected, result,
                         " a long list not completely sorted")

    # authors outlook
    def test_empty(self):
        argument = is_sorted([])
        expected = True
        self.assertEqual(expected, argument,
                         " the list is empty")

    def test_one_item(self):
        argument = is_sorted([1])
        expected = True
        self.assertEqual(expected, argument,
                         " the list has one item")

    def test_duplicates(self):
        """ test a sorted list with duplicate values. """
        argument = is_sorted([1, 2, 2, 3])
        expected = True
        self.assertEqual(expected, argument,
                         " the list has duplicate values")

    def test_not_sorted(self):
        argument = is_sorted([3, 2])
        expected = False
        self.assertEqual(expected, argument,
                         "the list has one item.")
        

    
unittest.main()
