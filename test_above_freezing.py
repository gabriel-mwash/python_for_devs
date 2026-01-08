import unittest
import temperature


class TestAboveFreezing(unittest.TestCase):
    """ Tests for temperature.above_freezing. """

    def test_above_freezing_above(self):
        """ Test a temp above freezing."""
        expected = True
        actual = temperature.above_freezing(5.2)
        self.assertEqual(expected, actual, "The temperature is above freezing.")

    def test_above_freezing_below(self):
        """ Test a temp below freezing."""
        expected = False
        actual = temperature.above_freezing(-2)
        self.assertEqual(expected, actual, "The temperature is below freezing.")

    def test_above_freezing_at_zero(self):
        """ Test a temperature that is at freezing. """
        expected = False
        actual = temperature.above_freezing(0)
        self.assertEqual(expected, actual,
                         "the temperature is at the freezing mark")


unittest.main()
