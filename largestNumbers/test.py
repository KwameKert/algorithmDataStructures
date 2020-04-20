import unittest

from code import largestThreeNumbers


class LargestNumberTestCase(unittest.TestCase):

    def test_first(self):
        result = largestThreeNumbers([4,1,3,2,9,8])
        self.assertEqual(result,[4,8,9])

    def test_second(self):
        result = largestThreeNumbers([-9,23,9,18,-2])
        self.assertEqual(result,[9,18,23])


if __name__ == '__main__':
    unittest.main()
