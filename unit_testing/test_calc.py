import unittest
import calc


# see for all test Methods: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class TestCalc(unittest.TestCase):

    def test_add(self):
        """test with `python -m unittest test_calc.py"""
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # test if dividing by zero raises an ValueError
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        # better to use Context Manager to raise exceptions
        with self.assertRaises(ValueError):
            calc.divide(10,0)


if __name__ == '__main__':
    unittest.main()