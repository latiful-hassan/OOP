
##############################
"""SUBCLASSES & INHERITANCE"""
##############################

"""
Inheritance allows us to inherit attributes and methods from parent class.
This means we can change the functionality of methods without altering the
code in the parent class.
"""


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


"""
Let's create a use case where we want new types of employees that
have the same information as our init method.
"""


class Developer(Employee):  # create subclass which inherits methods from Employee class

    raise_amount = 1.10  # specific raise amount for Developer subclass

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # applies to Employee init method, no need to repeat logic
        self.prog_lang = prog_lang  # lets Developer deal with prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):  # sets employees under the manager
        super().__init__(first, last, pay)  # super() refers to parent class
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print("--->", emp.fullname())


dev_1 = Developer("Corey", "Schafer", 50000, 'Python')
dev_2 = Developer("Test", "User", 60000, 'SQL')

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_employees()

# print(dev_1.email) #takes results from methods in Employee
# print(dev_1.prog_lang) #takes results from methods in Developer

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

"""
The 'help' function below will give us information such as what the
Developer class has inherited and the 'method resolution order' which
tells us where attributes and methods are being pulled from and in what
order. Therefore, if we place 'pass' in the block for the subclass, we
can still use all of the assets that are inherited.
"""

# class Developer(Employee):
#    pass

# print(help(Developer))

"""
Python has built-in functions called 'isinstance' and 'issubclass'.
"""

print(isinstance(mgr_1, Manager))  # checks is object (arg1) is an instance of the class (arg2)
print(issubclass(Developer, Employee))  # checks if a subclass (arg1) is a subclass of a parent class (arg2)
