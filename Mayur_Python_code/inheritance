class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = fname+lname+'@company.com'

    def emp_info(self):
        return self.email


class Employee(Person):
    def __init__(self, fname, lname, ID, Cell_No):
        Person.__init__(self, fname, lname)
        self.ID = ID
        self.Cell_No = Cell_No

    def get_emp_details(self):
        return self.emp_info() + ' ' + self.ID + ' ' + self.Cell_No


parent = Person('Sam', 'Robinson')
child = Employee('Robert', 'Wilson', '123', '27389476231')

print(parent.emp_info())
print(child.get_emp_details())
