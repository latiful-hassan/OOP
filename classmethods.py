
##################
"""CLASSMETHODS"""
##################


class Employee:

    raise_amount = 1.04
    num_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    """Can use a class instead of instance as an argument by creating
    a class method as seen below with the decorator, @classmethod."""

    """With a class method we want to act on the class (cls) instead
    of the instance (self)."""

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod  # Example Scenario answer
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # use cls instead of self to return new object


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

Employee.set_raise_amount(1.05)  # setting raise to all instances 5%, this acts on the class variable

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# ################
# Example Scenario
# ################

"""Below is a more procedural method of taking a hyphen-separated string
and parse through it in order for the string to be used with our methods."""

"""Instead of this we can created a new class method to automate this as seen 
in the above code as an alternative constructor."""

emp_str_1 = 'John-Doe-70000'  # need to split first
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)

"""Due to the new class method below we can fully automate the split."""

#    @classmethod
#        def from_string(cls, emp_str):
#            first, last, pay = emp_str.split('-')
#            return cls(first, last, pay)

new_emp_1_v2 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)
