import unittest
from code import anagrams


class TestAnagrams(unittest.TestCase):

    def test_first(self):
        result = anagrams('rail safety', 'fairy tales')
        self.assertTrue(result)

    def test_second(self):
        result = anagrams('RAIL! SAFETY!', 'fairy tales')
        self.assertTrue(result)

    def test_third(self):
        result = anagrams('Hi there', 'Bye there')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()


