class CountingChars(object):
    def __init__(self):
        self.input =''
        self.output=''

    def get_input(self):
        self.print_question()
        return input()

    def get_length(self,word):
        return len(word)

    def print_output(self,answer):
        return print(answer +" has " + str(self.get_length(answer)) + " characters")

    def print_question(self):
        print('What is the input string?')

class doCount(object):
    if __name__ == "__main__":
        a = CountingChars()
        a.print_output(a.get_input())