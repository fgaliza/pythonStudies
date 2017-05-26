class Strings(object):
    """docstring for Strings"""

    def __init__(self, arg):
        super(Strings, self).__init__()
        self.arg = arg

    def printRawString():
        """
        Printing like this, provides a way of ignoring special characters
        and just printing the string as is
        """
        print(r'C://File/test/')

    def splitString(string, start, end):
        """
        To get a slice of the string,
        just set start position followed by end position

        EX:
        starts and includes character at 2 position,
        and slices UNTIL it reaches the 7 position, not including it
        user[2:7] = llipe

        If you do not include the first part of the positioning,
        Python will assume you want it to start at the very beginning
        starting at the beginning and going until the 7th position
        user[:7] = Fillipe

        If you do not include the end portion of the positioning,
        it will start at the position given and go all the way
        until the end of the string

        user[3:] = lipe Galiza

        """

        return string[start:end]

    def stringLetter(string, position):
        """
        You can treat strings as multidimensional arrays in PHP.

        EX:
        user[5] = p
        user[-1] = a
        user[-2] = z
        """
        return string[position]

    def getStringLength(string):
        return len(string)
