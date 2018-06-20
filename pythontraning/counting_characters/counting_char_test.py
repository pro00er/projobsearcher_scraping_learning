import unittest
from pythontraning.counting_characters.counting_char import CountingChars


def fun(x):
    return x + 1

class CountCharTest(unittest.TestCase):



    def test_count_word_char_length(self):
        a = CountingChars()
        self.assertEqual(a.get_length('word'), 4)

