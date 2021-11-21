#########################
"""PROPERTY DECORATORS"""
#########################


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property  # creating 'getter', defining email in class like method, but can call as if an attr
    def email(self):
        return f"{self.first}.{self.last}'@company.com'"

    @fullname.setter  # creating 'setter' decorator
    def fullname(self, name):  # 'name' arg is the name we are trying to set in the ins. var.
        self.first, self.last = name.split(' ')

    @fullname.deleter  # creating 'deleter' decorator
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

# emp_1.first = 'Jim'

"""If we want to use an ins. var. to set fullname, but want it
to also change first and last, then we use a 'setter'"""

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname  # deleting fullname and replacing with None
