import unittest

from code import caesarEncryptor


class CaesarEncryptor(unittest.TestCase):

    def first_test(self):
        result = caesarEncryptor("xyz", 2)
        self.assertEquals(result, "zab")

    def second_test(self):
        result = caesarEncryptor("abc", 4)
        self.assertEquals(result, "def")


if __name__ == '__main__':
    unittest.main()
