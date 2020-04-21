from code import bubbleSort
import unittest

class bubbleSortTest(unittest.TestCase):

    def test_first(self):
        result = bubbleSort([9, 7, 2, 1, 0])
        self.assertEqual(result, [0, 1, 2, 7, 9])

    def test_second(self):
        result = bubbleSort([90, 60, 12, 1, 2, 4])
        self.assertEqual(result, [1, 2, 4, 12, 60, 90])


if __name__ == '__main__':
    unittest.main()
