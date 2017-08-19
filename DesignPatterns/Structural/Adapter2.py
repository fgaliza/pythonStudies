"""
Adapter!

Problem
	* Incompatible interfaces
"""

from abc import ABCMeta, abstractmethod


class Korean(object):

    def speak(self):
    	print("An-neyoung")


class English(object):

    def speak(self):
        print('Hello')


class Speaker(metaclass=ABCMeta):
    """docstring for Adapter"""

    def __init__(self, obj, method):
        self.obj = obj
        self.method = method

    def speak(self):
        getattr(self.obj, self.method)()

s1 = Speaker(Korean(), 'speak')
s2 = Speaker(English(), 'speak')
s1.speak()
s2.speak()
