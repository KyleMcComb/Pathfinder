import unittest  # You can use the unittest library for writing test cases
from main.requestFunctions.gradeInfo import *

class CalcAvgMarkTestCase(unittest.TestCase):

    def test_empty_list(self):
        # Test with an empty list
        arr = []
        result = calcAvgMark(arr)
        self.assertEqual(result, 0)

    def test_single_grade(self):
        # Test with a list containing a single grade
        arr = [{'mark': 90}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 90.0)

    def test_multiple_grades(self):
        # Test with a list containing multiple grades
        arr = [{'mark': 80}, {'mark': 90}, {'mark': 70}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 80.0)

    def test_zero_mark(self):
        # Test with a list containing a zero mark
        arr = [{'mark': 0}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 0.0)

    def test_mixed_grades_and_zeros(self):
        # Test with a list containing mixed grades and zeros
        arr = [{'mark': 75}, {'mark': 0}, {'mark': 85}, {'mark': 60}]
        result = calcAvgMark(arr)
        self.assertEqual(result, 55.0)

    def test_invalid_input(self):
        # Test with a list containing an invalid dictionary (missing 'mark' key)
        arr = [{'score': 80}, {'mark': 90}]  # One dictionary is missing the 'mark' key
        with self.assertRaises(KeyError):
            calcAvgMark(arr)

if __name__ == '__main__':
    unittest.main()
