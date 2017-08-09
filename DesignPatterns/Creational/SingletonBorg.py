"""
Singleton using the BORG Design Pattern!

Problem
    * Only one instance
	* Global variable in an object oriented way
"""


class Borg(object):
    """docstring for Borg"""

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):
    """docstring for Singleton"""
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)        

    def __str__(self):
        return str(self._shared_state)