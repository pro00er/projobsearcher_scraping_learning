import unittest

from pythontraning.parsingFile.parsing_file import ParsingFile

class ParsingFileTest(unittest.TestCase):
    def setUp(self):
        self.pf = ParsingFile()
        self.file = "Ling,Mai,55900"
        self.file_multiple_row = "Ling,Mai,55900\n Johnson,Jim,56500\nZarnecki,Sabrina,51500"

    def test_is_exist_comma_parsing(self):
        self.assertEqual(self.pf.parsing(self.file), ["Ling","Mai","55900"])

    def test_success_last_field_value(self):
        self.assertEqual(self.pf.get_last_value(self.file), "Ling")

    def test_success_first_field_value(self):
        self.assertEqual(self.pf.get_first_value(self.file), "Mai")

    def test_success_salary_field_value(self):
        self.assertEqual(self.pf.get_salary_value(self.file), "55900")

    def test_get_column_max_word_length(self):
        self.pf.get_column_max_word_length(self.file_multiple_row, 0)

# 결과값 확인이 아니라 파싱하고 있었음

    def test_각_열길이가_열에서_가장_긴_단어_더하기_공백_한글자인지_확인(self):
        row_num = 2
        self.assertEqual(self.pf.get_column_max_word_length(self.file_multiple_row,row_num), len("Zarnecki")+1)

    # def test_첫번째_열의_단어들_가져오는지_확인(self):
    #     self.pf.get_first_column_value(self.file_multiple_row)
        # self.assertEqual(self.pf.get_first_column_value(self.file_multiple_row), "Ling,Johnson,Zarnecki")





