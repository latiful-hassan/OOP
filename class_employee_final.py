
"""
This script is an example of creating a classes and subclasses for Employees,
Developers and Managers. We will set base attributes to Employees which is our parent class
and have Developers and Manager as subclasses.
"""

import datetime


class Employee:

    raise_amount = 1.04
    num_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_emps += 1

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted Name!')
        self.first = None
        self.last = None

    @property
    def email(self):
        return f"{self.first}.{self.last}'@company.com'"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f"'{self.fullname}' - '{self.email}'"

    def __add__(self, other):
        return self.pay + other.pay

    def __mul__(self, right):
        return self.pay * self.raise_amount

    def __len__(self):
        return len(self.fullname)


class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
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


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)
dev_1 = Developer("Corey", "Schafer", 50000, 'Python')
dev_2 = Developer("Test", "User", 60000, 'SQL')
mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
my_date = datetime.date(2016, 7, 10)
