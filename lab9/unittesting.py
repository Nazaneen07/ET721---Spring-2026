"""
Nazaneen Baguaei,
lab 9, unit testing
feb 26, 2026
"""
import unittest
from calculation import * 

# example 1: simple unit testing
def addtwonumbers(a, b):
    return a + b

# unit tests 
class TestAddFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(addtwonumbers(1, 2), 3) 
        # test that when pass 1 and 2, the return of the function is 3 

    # example 2: unit testing calculation.py file 
    def test_subtraction(self):
        self.assertEqual(subtracttwonumbers(6, 4), 2)
        self.assertEqual(subtracttwonumbers(4, 6), -2)
        self.assertEqual(subtracttwonumbers(5), 5)
        self.assertEqual(subtracttwonumbers(), 0)

    # unit test for multiplication function
    def test_multiplication(self):
        self.assertEqual(multiplythreenumbers(1, 2, 3), 6)
        self.assertEqual(multiplythreenumbers(1, -2, -3), 6)
        self.assertEqual(multiplythreenumbers(-1, -2, -3), -6)

    # unit test for division function 
    def test_division(self):
        self.assertEqual(dividetwonumbers(6, 3), 2)
        self.assertAlmostEqual(dividetwonumbers(10, 3), 3.3333, places=3)

    # unit test for division by zero and value error
    def test_divisionbyzero(self):
        # assertion none (not returning) or some known return value 
        self.assertIsNone(dividetwonumbers(10, 0))
        self.assertIsNone(dividetwonumbers(10, "a"))   # fixed: assertISnone → assertIsNone
        self.assertIsNone(dividetwonumbers("peter", 2)) # fixed: moved inside function

    # unit test for other possible errors by mocking
    def test_unexpected_exception(self):
        # expect an exception to occur
        with self.assertRaises(Exception):
            # passing no arguments to trigger an exception 
            dividetwonumbers()

if __name__ == "__main__":
    unittest.main()
