class Sets(object):
    """Sets are an object like a list, that accepts no duplicates"""

    def __init__(self, arg):
        super(Sets, self).__init__()
        self.arg = arg

    """
    If creating a set, I duplicate a value, it won`t generate error
    but the duplicate values simply will only show once
    """
    def createSet(arg1, arg2, arg3):
        mySet = {arg1, arg2, arg3}
        return mySet
