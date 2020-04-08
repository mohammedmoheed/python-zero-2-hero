"""Functions

In addition to using pre-defined functions, you can create your own functions by using the def statement.
Here is an example of a function named my_func. It takes no arguments, and prints "spam" three times. 
It is defined, and then called. The statements in the function are executed only when the function is called."""


def my_func():
    print("Hi")
    print("Moheed")
    print("here")


my_func()

"""Arguments

All the function definitions we've looked at so far have been functions of zero arguments, which are called with empty parentheses.
However, most functions take arguments.
The example below defines a function that takes one argument:"""


def function(argument):
    print(argument + "!")


function("hi")
function("hello")


# You can also define functions with more than one argument; separate them with commas.


def function(argument1, argument2):
    print(argument1 + argument2)
    print(argument1 * argument2)


function(5, 3)

""""Function arguments can be used as variables inside the function definition.
 However, they cannot be referenced outside of the function's definition.
 This also applies to other variables created inside a function."""


def function(variable):
    variable += 1
    print(variable)


function(2)
