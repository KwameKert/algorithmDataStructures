import unittest

from code import insertionSort


class InsertionSort(unittest.TestCase):

    def test_first(self):
        result = insertionSort([3, 0, 2, 1, 9, 7])
        self.assertEquals(result, [0, 1, 2, 3, 7, 9])

    def test_second(self):
        result = insertionSort([8, 5, 3, 2, 1])
        self.assertEquals(result, [1, 2, 3, 5, 8])


if __name__ == '__main__':
    unittest.main()
