import unittest
from pythontraning.counting_characters.counting_char import CountingChars

class CountCharTest(unittest.TestCase):
    def test_count_word_char_length(self):
        a = CountingChars()
        self.assertEqual(a.get_length('word'), 4)
