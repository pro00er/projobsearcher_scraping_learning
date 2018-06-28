import re


class inputVlaueCheck(object):

    def __init__(self):
        pass

    def check_value_name(self, label, answer):
        if answer is '':
            print("The "+label+" name must be filled in")
        elif len(answer) == 1:
            print("\""+answer+"\" is not a valid "+label+ " name. It is too short.")
        else:
            pass

    def input_name(self, label):
        a = input("Enter the "+label+" name:")
        self.check_value_name(label, a)

    def input_zip_code(self):
        answer = input("Enter the ZIP code:")
        p = re.compile('^[0-9]*$')
        m = p.match(answer)
        if m:
            pass
        else:
            print('The ZIP code must be numeric:' + answer)

    def input_employee_id(self):
        answer = input("Enter the Employee ID:")
        p = re.compile('([a-zA-Z]{1,2})\-([0-9]{4})')
        m = p.match(answer)
        if m:
            pass
        else:
            print(answer+' is not a valid ID')


class excute_init(object):
    if __name__ == "__main__":
        inputVal = inputVlaueCheck()
        inputVal.input_name("first")
        inputVal.input_name("last")
        inputVal.input_zip_code()
        inputVal.input_employee_id()
