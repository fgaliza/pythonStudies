"""
Factory!

Problem
	* Uncertainties in types of objects
	* Decisions to be made at runtime regarding what class to use
"""


class PetFactory(object):
    """docstring for PetFactory"""

    def __new__(self, arg):

        switcher = {
            "cat": Cat(),
            "dog": Dog()
        }
        try:
        	return switcher[arg]
        except KeyError:
        	print ("Pet not registered")

class Cat(object):
    """docstring for Cat"""

    def __init__(self):
        super(Cat, self).__init__()

    def speak(self):
        return "Meow!"


class Dog(object):
    """docstring for Dog"""

    def __init__(self):
        super(Dog, self).__init__()

    def speak(self):
        return "Woof!"

dog = PetFactory("dog")
print(dog.speak())
cat = PetFactory("cat")
print(cat.speak())