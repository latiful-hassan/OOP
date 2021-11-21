
"""
We can use classes to define our decorators instead of functions (see decorator_functions.py).
"""


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed before, {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


class DecoratorClass(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("call method executed before, {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display():
    print("Display Function Ran")


@DecoratorClass
def display_info(name, age):
    print("display_info ran with arguments {} {}".format(name, age))


display()
display_info("John", 25)
