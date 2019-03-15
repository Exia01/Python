import unittest
from robot import Robot  # import the class


class RobotTests(unittest.TestCase):
    def setUp(self):
        # create the class before each test
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.mega_man.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)

    def test_low_battery(self):
        self.mega_man.battery = -1
        self.assertEqual(
            self.mega_man.say_name(),
            "Low power.  Please charge and try again")
        self.assertEqual(self.mega_man.battery, -1)

    def test_learn_skill(self):
        print(self.mega_man.battery)
        """ Test for learning new skill """
        self.assertEqual(self.mega_man.learn_skill("Cooking", 30), "WOAH. I KNOW COOKING")
        self.assertEqual(self.mega_man.battery, 20)

if __name__ == "__main__":
    unittest.main()
