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
