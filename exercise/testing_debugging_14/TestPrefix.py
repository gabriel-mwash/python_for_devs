import unittest
import prefix



class TestPrefix(unittest.TestCase):
    """ tests for prefix.all_prefix """

    def test_prefix_empty(self):
        """ test for an empty string """
        expected = set()
        result = prefix.all_prefixes("")
        self.assertEqual(expected, result,
                         " the string is empty ")

    def test_prefix_non_string(self):
        """ test for a non string """
        expected = "this is not a string"
        result = prefix.all_prefixes(13)
        self.assertEqual(expected, result,
                         " a non string given ")

    def test_prefix_one_string(self):
        """ test for a 1 char string """
        expected = {"l"}
        result = prefix.all_prefixes("l")
        self.assertEqual(expected, result,
                         " a one char string ")

    def test_prefix_a_long_string(self):
        expected = {"l", "le", "lea", "lead", "leade", "leader", "leaders"}
        result = prefix.all_prefixes("leaders")
        self.assertEqual(expected, result,
                         " this is a long string ")


    # outhors part / code

    def test_single_char(self):
        """ test 1 char string. """
        argument = prefix.all_prefixes("x")
        expected = {"x"}
        self.assertEqual(expected, argument,
                         "Argument is a 1 char string.")

    def test_empty(self):
        """ test a on empty string """
        argument = prefix.all_prefixes("")
        expected = set()
        self.assertEqual(expected, argument,
                         "Argument is an empty string")

    def test_word(self):
        """ test a word with unique letters """
        argument = prefix.all_prefixes("water")
        expected = {"w", "wa", "wat", "wate", "water"}
        self.assertEqual(expected, argument,
                         " Argument is a word with unique letters")

    def test_mulitiple(self):
        """" test a word with multiple occurences of the first letter. """
        argument = prefix.all_prefixes("puppet")
        expected = {"p", "pu", "pup", "pupp", "puppe", "puppet"}
        self.assertEqual(expected, argument,
                         " firt letter occurs mulitiple times")


unittest.main()
