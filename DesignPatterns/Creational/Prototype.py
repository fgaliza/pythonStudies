import copy
"""
Prototype!

Problem
	* Creating many identical objects individually is expensive
	* Cloning is an alternative
"""


class Prototype(object):

    def __init__(self):
        self.objects = {}

    def register_object(self, name, obj):
        self.objects[name] = obj

    def unregister_object(self, name):
        del self.objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self.objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car(object):

    def __init__(self):
        self.name = "Ford"
        self.color = "Red"
        self.options = "EX"

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object('ford', c)

c1 = prototype.clone('ford')

print(c1)
