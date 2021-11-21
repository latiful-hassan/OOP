
"""
Below is an example of a first-class function, which means we can treat a function
like an object. This means we can pass functions as arguments to other functions, return functions
and assign functions to variables.
"""


def outer_function():
    message = "Hi"

    def inner_function():
        print(message)
    return inner_function  # take parens off to not call the func


my_func = outer_function()  # setting the function to a varible as if it was an object

"""
Below is a closure, it allows us to have an inner function that remembers variables local to
the scope in which they were created. So even after the outer function has executed, it remembers
the variable - 'free-variable'.
"""

my_func()

##############################

"""
Now let's pass in arguments.
"""


def outer_function(msg):
    message = msg

    def inner_function():
        print(message)
    return inner_function


hi_func = outer_function("Hi")
bye_func = outer_function("Bye")
hi_func()
bye_func()

##############################

"""
Since we can nest our functions together, we can simplify the above code.
"""


def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function
