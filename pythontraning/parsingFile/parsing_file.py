class ParsingFile(object):
    def __init__(self):
        self.input =''
        self.output=''

    def parsing(self, file):
        return file.split(",")

    def get_last_value(self, file):
        return file.split(",")[0]

    def get_first_value(self, file):
        return file.split(",")[1]

    def get_salary_value(self, file):
        return file.split(",")[2]

    def get_column_length(self, file, row_num):
        return len(file.split("\n")[row_num])
    #TODO 열에서 가장 긴단어

    def get_first_column_value(self, file_multiple_row):
        row_array = file_multiple_row.split("\n")

        for row in row_array:
            print(row.split(",")[0])

    def get_column_max_word_length(self, file_multiple_row, row_num):
        target_row = file_multiple_row.split("\n")[row_num]
        target_words = target_row.split(",")
        self.get_max_word_length(target_words)

    def get_max_word_length(self, words):
        return len(max(words, key=len))
