import unittest
from palindrome import Palindrome

p1 = Palindrome()

class testPalindrome(unittest.TestCase):
    def test_true(self):
        self.assertEqual(p1.palindrome('aba'), True)
        self.assertEqual(p1.palindrome('abba'), True)
        self.assertEqual(p1.palindrome('abcba'), True)
        self.assertEqual(p1.palindrome('1234321'), True)
        self.assertEqual(p1.palindrome('&*()(*&'), True)

    def test_false(self):
        self.assertEqual(p1.palindrome('ab'), False)
        self.assertEqual(p1.palindrome('abca'), False)
        self.assertEqual(p1.palindrome('1234'), False)
        self.assertEqual(p1.palindrome('&*(*&&%*&56'), False)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            p1.palindrome(1)
            p1.palindrome(1.0)
            p1.palindrome(30000000000)

if __name__ == '__main__':
    unittest.main()