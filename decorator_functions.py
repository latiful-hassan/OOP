"""
A Decorator is a function that takes another function as an argument, adds some functionality,
then returns another function - all without altering the source code of the original function
that was passed in. This behavior is quite similar to first-class functions/closures.
"""


def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def display():  # the decorator above does not alter this function at all
    print("Display Function Ran")


decorated_display = decorator_function(display)

"""
Below is equal to wrapper_function which is waiting to be executed, which then returns 
the original_function.
"""

decorated_display()

###############

"""
The reason we use decorators, is because we can add additional functionality
within the wrapper portion of our code.
"""


def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before, {}".format(original_function.__name__))
        return original_function()
    return wrapper_function


@decorator_function  # adding this syntax means we can call display() with all additional functionality
def display():
    print("Display Function Ran")


decorated_display = decorator_function(display)
decorated_display()

display()  # this is equal to display = decorator_function(display)

###############

"""
We cannot use the @decorator_function with other functions as we did no previously allow
any number of arguments, below this is adjusted.
"""


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed before, {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display_info(name, age):
    print("display_info ran with arguments {} {}".format(name, age))


display_info("John", 25)
