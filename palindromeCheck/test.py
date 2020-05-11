import unittest

from code import palindromeCheck



class palindromCheckTestCase(unittest.TestCase):

    def first_test(self):
        result = palindromeCheck("abba")
        self.assertTrue(result)

    def second_test(self):
        result = palindromeCheck("accb")
        self.assertFalse(result)

    def third_test(self):
        result = palindromeCheck("cccc")
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()

