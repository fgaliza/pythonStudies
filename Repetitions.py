class Repetitons(object):
    """docstring for Repetitons"""

    def __init__(self, arg):
        super(Repetitons, self).__init__()
        self.arg = arg

    def forLoop(myList, start, end):
        """
        list = ['bacon', 'tuna', 'ham', 'sausages', 'beef']
        """

        for x in myList[start:end]:
            print(x)
            print(len(x))
            pass

    def rangeLoop(start, end, increment):
        for x in range(start, end, increment):
            print('banana')

    def whileLoop(start=1, end=10):

        while start < end:
            print('lool')
            start += 1

    def magicNumber(number=3):
        for x in range(101):
            if x is number:
                print(x, ' is the magic number')
                break
            else:
                continue