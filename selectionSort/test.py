import unittest

from code import selectionSort

class SelectionSort(unittest.TestCase):

    def test_first(self):
        result = selectionSort([9, 8, 7, 2, 1])
        self.assertEquals(result, [1, 2, 7, 8, 9])

    def test_second(self):
        result = selectionSort([10, 98, 1, 0])
        self.assertEquals(result, [0, 1, 10, 98])


if __name__ == '__main__':
    unittest.main()

