class Conditions(object):
    """docstring for Conditions"""

    def __init__(self, arg):
        super(Conditions, self).__init__()
        self.arg = arg

    def ifelse(param1, param2):

        if param1 > param2:
            print "%s is bigget than %s" % (param1, param2)
        elif param2 < param1:
            print "%s is bigget than %s" % (param2, param1)
        else:
            print "The values are equal"

    def checkIfSameObject(param1, param2):

        """
        Compare memory location of two objects
        Check if the variables on either side of the operator
        point to the same object
        """

        if param1 is param2:
            print 'YES'
        else:
            print 'NO'

