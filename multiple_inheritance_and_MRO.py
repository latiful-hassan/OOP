
##########################
"""MULTIPLE INHERITANCE"""
##########################

"""
Classes can inherit from multiple sources. These sub-classes will inherit methods from
all of their parents.

The order in which the parent classes are implemented will affect the output of any
shared methods (e.g. 'greet' method, in the below case, Ambulatory's greet takes priority).
"""


class Aquatic:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"I am {self.name} of the SEA!"


class Ambulatory:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"I am {self.name} of the LAND!"


class Penguin(Ambulatory, Aquatic):  # this order matters!

    def __init__(self, name):
        super().__init__(name=name)


pengwing = Penguin("Pingu")
print(pengwing.greet())  # prints from 'Ambulatory' as it's referenced before 'Aquatic' in subclass

###################################
"""METHOD RESOLUTION ORDER (MRO)"""
###################################

"""
When a class is created, Python sets a 'Method Resolution Order', MRO, for that class, which is the 
order in which Python will look for methods on instances of that class.
"""

# To see MRO:
#            cls.__mro__
#            cls.mro()
#            help(cls)


class A:

    def do_something(self):
        return f"Method Defined In: A"


class B(A):
    pass


class C(A):

    def do_something(self):
        return f"Method Defined In: C"


class D(B, C):
    pass


thing = D()
print(thing.do_something())  # prints from C as D and B have pass, so C is next in MRO
