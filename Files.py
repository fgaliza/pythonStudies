class Files(object):
    """docstring for Files"""

    def __init__(self, arg):
        super(Files, self).__init__()
        self.arg = arg

    def writeFile(fileName, text):
        fw = open(fileName, 'w')
        fw.write(text)
        fw.close()

    def readFile(fileName):
        fr = open(fileName, 'r')
        text = fr.read()
        print(text)
        pass


files = Files
files.writeFile('sample.txt', 'This is a sample text')
files.readFile('sample.txt')
