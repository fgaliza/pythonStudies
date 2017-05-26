class Conditions(object):
    """docstring for Conditions"""

    def __init__(self, arg):
        super(Conditions, self).__init__()
        self.arg = arg

    def ifelse():
        n1 = 1
        n2 = 2
        string1 = "Hello"
        string2 = "How are you?"
        """
    	Straight forward if else logic
    	"""
        if n1 > n2:
            print('n1 bigger')
        else:
            print('n2 bigger')

        if string1 is "Fillipe":
        	print('Hello Fillipe')
        elif string1 is  "Lucy":
        	print ("Hello Lucy")
        elif string1 is "Gabe":
        	print ("Hello Gabe")
        else:
        	print("Who are you?")

