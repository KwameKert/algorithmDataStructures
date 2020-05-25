import unittest

from code import twoNumber

class TwoNumberTestCase(unittest.TestCase):

    def test_first(self):
        result = twoNumber([1,-2,3,5,-9],1 )
        self.assertEqual(result, [-2, 3])

    def test_second(self):
        result = twoNumber([2, 4, -5, 8, -10], 3)
        self.assertEqual(result, [-5, 8])

    def test_third(self):
        result = twoNumber([3, 2, 5 -6, 9], 10)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main();
