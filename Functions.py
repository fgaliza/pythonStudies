class Functions(object):
    """docstring for Functions"""

    def __init__(self, arg):
        super(Functions, self).__init__()
        self.arg = arg

    def randomString(firstWord="Testing", secondWord="Default", thirdWord="values"):

        print(firstWord, " ", secondWord, " ", thirdWord)

    def addingCalculator(*args):
        total = 0
        for i in args:
            total += i
        print(total)

    def unpackingArgs(arg1, arg2, arg3):
        return arg1 + arg2 + arg3


"""
You can passa the parameters in any order, if you especify
which one you are setting
"""
functions = Functions()
functions.randomString(secondWord="am", firstWord="I", thirdWord="awesome")
"""
The way this function was defined, it can receive any number
of parameters, being from one to infinity, and store them all
into the args variable
The adding Calculator function will break if it receives a string
"""
functions.addingCalculator(3)  # prints 3
functions.addingCalculator(1, 1, 1, 1, 1, 1, 1, 1, 1,
                           1, 1, 1, 1, 1, 1, 1)  # prints 16
"""
The function 'Unpacking Args' needs 3 values to work
They can be passed as a list if you add a * to tell python
that the argument being passed on the function is a list
THIS ONLY WORKS IF THE NUMBER OF ARGS IN THE LIST IS THE SAME
AS THE NUMBER NEEDED IN THE FUNCTION, NO MORE, NO LESS
"""
myList = [1, 2, 3]
functions.unpackingArgs(*myList)
