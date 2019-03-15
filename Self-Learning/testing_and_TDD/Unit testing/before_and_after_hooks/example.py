# To run we only have to execute test.py or -v at end for comments or more info
import unittest


class SomeTests(unittest.TestCase):
    def setUp(self):
        # do some setup here
        pass

    def test_first(self):
        # setUp runs before
        # tearDown runs after
        pass

    def test_second(self):
        # setUp runs before
        # tearDown runs after
        pass

    def tearDown(self):
        # do tearDown here
        pass


#setup will run before test_first and test_second

#tearDown will run after test_first and test_second