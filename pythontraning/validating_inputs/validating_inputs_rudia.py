import re


class inputVlaueCheck(object):

    def __init__(self):
        pass

    def check_value_name(self, label, answer):
        if answer is '':
            print("The "+label+" name must be filled in")
        elif len(answer) == 1:
            print("\""+answer+"\" is not a valid "+label+ " name. It is too short.")

    def enter_name(self, label):
        a = input("Enter the "+label+" name:")
        self.check_value_name(label, a)

    def enter_zip_code(self):
        answer = input("Enter the ZIP code:")
        p = re.compile('^[0-9]*$')
        m = p.match(answer)
        if not m:
            print('The ZIP code must be numeric:' + answer)

    def enter_employee_id(self):
        answer = input("Enter the Employee ID:")
        p = re.compile('([a-zA-Z]{1,2})\-([0-9]{4})')
        m = p.match(answer)
        if not m:
            print(answer+' is not a valid ID')


class excute_init(object):
    if __name__ == "__main__":
        inputVal = inputVlaueCheck()
        inputVal.enter_name("first")
        inputVal.enter_name("last")
        inputVal.enter_zip_code()
        inputVal.enter_employee_id()

