# To run we only have to execute test.py or -v at end for comments or more info
import unittest
from activities import eat, nap, is_funny, laugh  # importing the functionalities


# setting up the test

class ActivityTests(unittest.TestCase):  # Can be named anything. Inherits from class
    # def test_no_eat(self):
    #     """ Eat should have a positive message for healthy eating """
    #     self.assertEqual(eat("", is_healthy=None),
    #                      "I'm not really hungry")

    def test_eat_healthy(self):
        """ Eat should have a positive message for unhealthy eating """
        self.assertEqual(eat("broccoli", is_healthy=True),
                         "I'm eating broccoli, because my body is a temple")

    def test_eat_unhealthy(self):
        self.assertEqual(eat("pizza", is_healthy=False),
                         "I'm eating pizza, because YOLO")

    def test_eat_boolean(self):
        """ No value error passed """
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")

    def test_short_nap(self):
        """Short naps should be refreshing"""
        self.assertEqual(nap(1), "I'm feeling refreshed after my 1 hour nap")

    def test_long_nap(self):
        """Long naps should not discouraging"""
        self.assertEqual(
            nap(3), "Ugh I overslept. I didn't mean to nap for 3 hours!")


class IsFunnyTest(unittest.TestCase):
    def test_is_funny_tim(self):
        # Checks both and absolutely false
        self.assertEqual(is_funny("Tim"), False)
        # below assumes false and adds message
        # may passed because it is falsey
        self.assertFalse(is_funny("Tim"), "Tim should not be funny")

    def test_is_funny_anyone_else(self):
        # can have multiple if testing same thing or similar
        """ Anyone else but Tim should be funny """
        self.assertTrue(is_funny("Kim"), "Kim should be funny")
        self.assertTrue(is_funny("Tom"), "Tom should be funny")
        self.assertTrue(is_funny("Kathy"), "Kathy should be funny")

    def test_laugh(self):
        # any of those value are in the tuple
        self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))


if __name__ == "__main__":
    unittest.main()  # this will run our test
