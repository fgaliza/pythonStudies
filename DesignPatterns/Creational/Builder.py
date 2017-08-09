"""
Builder!

Problem
	* Excessive number of constructors 
"""


class Director(object):

    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.create_new_car()
        self.builder.add_model()
        self.builder.add_tires()
        self.builder.add_engine()

    def get_car(self):
        return self.builder.car


class Builder(object):

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class FerrariBuilder(Builder):

    def add_model(self):
        self.car.model = "Ferrari"

    def add_tires(self):
        self.car.tires = "Regular Tires"

    def add_engine(self):
        self.car.engine = "Turbo Engine"


class MercedesBuilder(Builder):

    def add_model(self):
        self.car.model = "Mercedes"

    def add_tires(self):
        self.car.tires = "Super Tires"

    def add_engine(self):
        self.car.engine = "Normal Engine"


class Car(object):

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)

builder = MercedesBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)
