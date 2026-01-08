import unittest
import double_preceding


class TestRunning_doublePreceding(unittest.TestCase):
    """ test for double_preceding """
    

    def test_identical(self):
        argument = [1, 1, 1]
        expected = [0, 2, 2]
        double_preceding.double_preceding(argument)
        self.assertEqual(expected, argument,
                         """ the list has multiple identical values""")

    def test_double_preceding_empty(self):
        """ test for an empty list """
        
        argument = []
        expected = []
        double_preceding.double_preceding(argument)
        self.assertEqual(expected, argument,
                         """the list is empty""")

    def test_double_preceding_one_item(self):
        """ test for one item """
        argument = [1]
        expected = [0]
        double_preceding.double_preceding(argument)
        self.assertEqual(expected, argument,
                         """ the list has one item """)

    def test_double_preceding_zero_items(self):
        argument = [0, 0, 0]
        expected = [0, 0, 0]
        double_preceding.double_preceding(argument)
        self.assertEqual(expected, argument,
                         """ the list has zero items """)

    def test_double_preceding_two_item(self):
        """ test for two items """
        argument = [4, 3]
        expected = [0, 8]
        double_preceding.double_preceding(argument)
        self.assertEqual(expected, argument,
                         """ the list has two items""")

    def test_double_preceding_positive_items(self):
        argument = [2, 4, 6, 7]
        expected = [0, 4, 8, 12]
        double_preceding.double_preceding(argument)
        self.assertEqual(expected, argument,
                         """ the list has positive values """)

    def test_double_preceding_negative_items(self):
        argument = [-2, -3, -5, -7]
        expected = [0, -4, -6, -10]
        double_preceding.double_preceding(argument)
        self.assertEqual(expected, argument,
                                          """ the list has negative values """)

    def test_double_preceding_mixed_items(self):
        argument = [4, -1, 3, -7, 6]
        expected = [0, 8, -2, 6, -14]
        double_preceding.double_preceding(argument)
        self.assertEqual(expected, argument,
                                          """ the list has mixed values """)



unittest.main()
