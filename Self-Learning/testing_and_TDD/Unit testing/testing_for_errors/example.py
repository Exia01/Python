# To run we only have to execute test.py or -v at end for comments or more info
import unittest


class SomeTest(unittest.TestCase):
    """ Testing for an error """

    def testing_for_error(self):
        with self.assertRaises(IndexError):
            l = [1, 2, 3]
            l[100]
