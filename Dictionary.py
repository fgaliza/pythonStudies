class Dictionary(object):
    """Dictionary is a python object similar to an associative array in PHP"""

    def __init__(self, arg):
        super(Dictionary, self).__init__()
        self.arg = arg

    def createDictionary():
        dictionary = {'key1': 'value1', 'key2': 'value2'}
        """
        This way of writing the FOR LOOP considers both the key
        and value of the dictionary, so you can use both variables
        for each dictionary item
        """
        for key, value in dictionary.items():
            print(key + " " + value)
