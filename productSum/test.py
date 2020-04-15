import unittest

from code import productSum

class ProductTestCase(unittest.TestCase):

    def test_product_sum(self):
        result = productSum([5,2,[7,-1],3,[6,[-13,8],4]])
        self.assertEqual(result,18)

    def test_product(self):
        result = productSum([3, 3, [3, 5, 5], 8])
        self.assertEqual(result,40 )


if __name__ == '__main__':
        unittest.main()
