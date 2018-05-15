class Book ():
    def __init__(self, name, author, date):
        self.name = name
        self.author = author
        self.date = date


book1 = Book ('XYZ', 'Mayur', '12 April 1999')
book1.author = 'nabvdf'
print (book1.author)


class P:
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x


p1 = P(42)
p2 = P(2456)
print(p1.get_x ())
p1.set_x(p2.x)
print(p1.get_x ())


class Employee:
    raise_amt = 2.4

    def __init__(self, fname, lname, sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal
        self.email = fname + lname + '@company.com'

    def fullname(self):
        return '{}{}'.format(self.fname, self.lname)

    def raise_calculation(self):
         # self.sal = int(self.sal * self.raise_amt)  #using instance variable
         self.sal = int(self.sal * Employee.raise_amt)# using class variable

    def salary(self):
        return self.sal

    def email(self):
        return self.email


emp1 = Employee('Sam', ' Robert', 50000)
emp2 = Employee('Dev', 'Bishoph', 32435)
print(emp1.fullname())# using object instance with  function
print(Employee.salary(emp2))#using class instance with object instance as argument
print(Employee.email(emp2))
print(emp1.sal)
print(emp2.sal)
emp1.raise_calculation()
emp2.raise_calculation()
print(emp1.sal)
print(emp2.sal)


