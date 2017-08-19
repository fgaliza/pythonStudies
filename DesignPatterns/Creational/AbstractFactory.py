"""
Abstract Factory!

Problem
	* The user expectation yields multiple, related objects
"""


class PetStore(object):
    """docstring for PetFactory"""

    def __init__(self, pet_factory=None):

        self.pet_factory = pet_factory

    def show_pet(self):

        pet = self.pet_factory.get_pet()
        pet_food = self.pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'!".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))


class Cat(object):
    """docstring for Cat"""

    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"


class CatFactory(object):
    """docstring for CatFactory"""

    def get_pet(self):
        return Cat()

    def get_food(self):
        return "Cat Food!"


class Dog(object):
    """docstring for Dog"""

    def __str__(self):
        return "Dog"

    def speak(self):
        return "Woof!"


class DogFactory(object):
    """docstring for DogFactory"""

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food!"


factory = CatFactory()
shop = PetStore(factory)
shop.show_pet()