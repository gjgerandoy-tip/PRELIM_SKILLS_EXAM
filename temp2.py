from typing import ValuesView
from temp import Temperature
import unittest

class answer(unittest.TestCase):

    def test(self):
        with self.assertRaises(ValueError): #First Successful test
            Temperature(-3)

    def test2(self):
        with self.assertRaises(ValueError): #To test if it will receive an error
            Temperature(1)

    def test3(self):
        with self.assertRaises(ValueError): #Second Successful test
            Temperature(1,3)

    def test4(self):
        with self.assertRaises(ValueError): #Third Successful test
            Temperature()


if __name__ == '__main__':
    unittest.main()
        
