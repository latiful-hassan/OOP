
"""Classes allow us to logically group our functions, that can
make it easier for the end-user to use and build upon. They are
blueprints for instantiating instances of the class (objects)."""

"""A method in the below contexts are just functions used by classes."""


class Employee:

    """Below is a class variable which are shared by all instances
    and can be accessed by instances but can be overridden via instance variables.
    For example if you wanted to modulate the raise_amount for individual employees.
    You would then use the apple_raise method."""

    raise_amount = 1.04  # class variable

    num_emps = 0  # making class variable of number of employees (see init method)

    """Below is the init method which is created with each instance of 
    'Employee' we call this the 'Constructor'."""

    def __init__(self, first, last, pay):  # blueprint of all attr needed for all employees
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_emps += 1  # this adds one to num_emps with every instantiation

    def fullname(self):  # self is the only arg as we want to refer to instance only
        return f"{self.first} {self.last}"  # putting self. means we don't need to specify name in object

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # applies raise specific to instance


# emp_1.raise_amount = 1.05 <- this applies specific raise and overrides the class variable

"""The comment below is an instance varible, it lies outside the class and is 
legal, however, we can automate this by giving the method its own attributes within 
the class which results in the below code."""

# emp.first = "Kasey" <- instance variable

emp_1 = Employee("Corey", "Schafer", 50000)  # automated via methods in class

"""The second line is what the first line becomes in the background.
'emp_1' gets passed in as an argument which shows what 'self' is."""

print(emp_1.fullname())
print(Employee.fullname(emp_1))

print(emp_1.__dict__)  # this shows the namespace in dictionary form
