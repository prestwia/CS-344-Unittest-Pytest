import unittest
from wordCount import wordCount

w1 = wordCount()

class testPalindrome(unittest.TestCase):
    def test_count(self):
        self.assertEqual(w1.wordCount('Hello'), 1)
        self.assertEqual(w1.wordCount('My name is.'), 3)
        self.assertEqual(w1.wordCount('This sentence has five words.'), 5)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            w1.wordCount(1)
            w1.wordCount(1.0)
            w1.wordCount(30000000000)

if __name__ == '__main__':
    unittest.main()