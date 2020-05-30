import unittest

from code import smallestDifference


class SmallestDifference(unittest.TestCase):

    def test_first(self):
        result = smallestDifference([-3, 7, 2, 9], [20, 4, 1, 5])
        self.assertEqual(result, [2, 1])

    def test_second(self):
        result = smallestDifference([1, 6, -10, 15], [3, 4, 23, 7, 90])
        self.assertEqual(result, [6, 7])


if __name__ == "__main__":
    unittest.main()
