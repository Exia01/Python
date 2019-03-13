# To run we only have to execute test.py or -v at end for comments or more info
import unittest
from activities import eat, nap  # importing the functionalities


# setting up the test

class ActivityTests(unittest.TestCase):  # Can be named anything. Inherits from class
    def test_no_eat(self):
        """ Eat should have a positive message for healthy eating """
        self.assertEqual(eat("", is_healthy=None),
                         "I'm not really hungry")
    def test_eat_healthy(self):
        """ Eat should have a positive message for unhealthy eating """
        self.assertEqual(eat("broccoli", is_healthy=True),
                         "I'm eating broccoli, because my body is a temple")

    def test_eat_unhealthy(self):
        self.assertEqual(eat("pizza", is_healthy=False),
                         "I'm eating pizza, because YOLO")

    def test_short_nap(self):
        """Short naps should be refreshing"""
        self.assertEqual(nap(1), "I'm feeling refreshed after my 1 hour nap")

    def test_long_nap(self):
        """Long naps should not discouraging"""
        self.assertEqual(
            nap(3), "Ugh I overslept. I didn't mean to nap for 3 hours!")


if __name__ == "__main__":
    unittest.main()  # this will run our test
