import unittest

from pythontraning.parsingFile.parsing_file import ParsingFile

class ParsingFileTest(unittest.TestCase):
    def setUp(self):
        self.pf = ParsingFile()
        self.file = "Ling,Mai,55900"

    def test_is_exist_comma_parsing(self):
        self.assertEqual(self.pf.parsing(self.file), ["Ling","Mai","55900"])

    def test_success_last_field_value(self):
        self.assertEqual(self.pf.get_last_value(self.file), "Ling")

    def test_success_first_field_value(self):
        self.assertEqual(self.pf.get_first_value(self.file), "Mai")

    def test_success_salary_field_value(self):
        self.assertEqual(self.pf.get_salary_value(self.file), "55900")


