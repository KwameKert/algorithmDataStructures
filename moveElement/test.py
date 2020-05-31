import unittest

from code import moveElement


class move_element(unittest.TestCase):

    def test_first(self):
        result = moveElement([2, 1, 2, 2, 2, 2, 3, 4, 5, 2], 2)
        self.assertEqual(result, [5, 1, 4, 3, 2, 2, 2, 2, 2, 2])

    def test_second(self):
        result = moveElement([4, 2, 1, 5, 2, 3, 7, 10, 2, 5, 7],7 )
        self.assertEqual(result, [4, 2, 1, 5, 2, 3, 5, 10, 2, 7, 7])


if __name__ == "__main__":
    unittest.main()
