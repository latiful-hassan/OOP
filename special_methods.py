class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f"{self.first}' '{self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    """
    repr() aims to be unambiguous | str() aims to be readable
    """

    def __repr__(self): #commonly used for debugging, reserved for devs
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')" #string to re-create object

    def __str__(self): #shown to end user
        return f"'{self.fullname}' - '{self.email}'"

    def __add__(self, other): #tells py how to add emps salaries together
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

# Below are calling the __repr__ and __str__ special methods
#print(repr(emp_1))
#print(str(emp_1))

print(emp_1 + emp_2)

print(len(emp_1))

