import unittest

from code import threeNumber


class threeNumberSumTestCase(unittest.TestCase):

    def first_test(self):
        result = threeNumber([-9, -4, -2, -1, 1, 2, 5, 4],-3 )
        self.assertTrue(result, [[-2, -1, 0 ], [-9, 2, 4]])

    def second_test(self):
        result = threeNumber([-5, -4, -3, -2, -1, 0, 1, 2, 3, 5, 6, 7],3 )
        self.assertTrue(result, [[-5, 1, 7], [-2, 0, 5], [0, 1, 2], [-3, 0, 6], [-3, -1, 7]])

    def third_test(self):
        result = threeNumber([0, 1, 2, 3, 4, 5], 90)
        self.assertTrue(result, [])

if __name__ == '__main__':
    unittest.main()
