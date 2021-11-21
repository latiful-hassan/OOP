
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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    """Regular methods pass the instance, 'self', as the first argument. Class methods pass
    the class, 'cls', as the first argument. Static methods do not pass anything
    automatically. They behave like regular functions but add logical connection to the class."""

    """Static methods have a limited use case, as they cannot access the properties
    of classes themselves. They are used if you need a utility function that 
    doesn't access class properties but still needs to belong to the class."""

    """If the instance or class is not used anywhere within a function, it
    is a static method. Therefore, you should use a static method if the code
    is not dependant on instance creation and does not use any instance variable."""

    """Create a function that takes a date and checks if it is a workday.
    In Python, days have indexes 0-6 for Mon-Sun."""

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: #checks if weekend
            return False
        else:
            return True


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

import datetime
my_date = datetime.date(2016, 7, 10) #prints false as it is a Sunday
print(Employee.is_workday(my_date))






