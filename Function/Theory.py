
"""Global Scope""" #Global Scope. The variables that are declared in the global scope can be accessed from anywhere
#               in the program.

# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.


"""Nonlocal keyword"""
# In Python, nonlocal keyword is used in the case of nested functions. This keyword works similar to the global,
# but rather than global, this keyword declares a variable to point to the variable of outside enclosing function,
# in case of nested functions.


"""Local variable""" #In Python or any other programming languages, the definition of local variables remains the same,
# which is “A variable declared inside the function is called local function”. We can access a local variable inside
# but not outside the function.


"""5 Types of Arguments in Python Function Definitions"""
# default arguments.
# keyword arguments.
# positional arguments.
# arbitrary positional arguments.
# arbitrary keyword arguments.


"""Variable-length arguments"""
# Variable-length arguments are also known as arbitrary arguments. If we don’t know the number of arguments needed
# for the function in advance, we can use arbitrary arguments
#
"""Two types of arbitrary arguments"""

#arbitrary positional arguments
#arbitrary keyword arguements

"""arbitrary positional arguments:"""
# For arbitrary positional argument, an asterisk (*) is placed before a parameter in function definition which can
# hold non-keyword variable-length arguments. These arguments will be wrapped up in a tuple. Before the variable
# number of arguments, zero or more normal arguments may occur.

"""arbitrary keyword arguments:"""
# For arbitrary positional argument, a double asterisk (**) is placed before a parameter in a function which can
# hold keyword variable-length arguments.

"""special paramters"""
# Positional or keyword arguments
# Positional only parameters
# Keyword-only argument


"""counter and most common"""
# The Counter() function returns a dictionary which is unordered. You can sort it according to the number of counts
# in each element using most_common() function of the Counter object. You can see that most_common function returns
# a list, which is sorted based on the count of the elements