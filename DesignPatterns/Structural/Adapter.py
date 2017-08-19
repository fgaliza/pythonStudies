"""
Adapter!

Problem
	* Incompatible interfaces
"""


class Korean(object):

    def __init__(self):
        self.name = 'Korean'

    def speak_korean(self):
        return "An-neyoung"


class English(object):

    def __init__(self):
        self.name = 'English'

    def speak_english(self):
        return 'Hello'


class Adapter(object):
    """docstring for Adapter"""

    def __init__(self, object, **adaptedMethod):
        self.object = object
        self.__dict__.update(adaptedMethod)

    def __getattr__(self, attr):
        return getattr(self.object, attr)

objects = []

korean = Korean()
english = English()

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(english, speak=english.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))
