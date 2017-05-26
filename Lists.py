class Lists(object):
    """docstring for Lists"""

    def __init__(self, arg):
        super(Lists, self).__init__()
        self.arg = arg

    def createNumberList(n1, n2, n3, n4, n5):
        numberList = [n1, n2, n3, n4, n5]
        return numberList

    def changeListValue(myList, position, newValue):
        myList[position] = newValue
        return myList

    def addLists(list1, list2):
        """
        Lists can magically be added to one another
        The result will be a giant list consisting
        litterally of a combination of list1 and list2
        where all the values of list2 will be positioned
        at the end of list1

        EX:
        list1 = [1, 2, 3, 4]
        list2 = [5, 6, 7, 8]

        list1 + list2 = [1,2,3,4,5,6,7,8]

        """
        list3 = list1 + list2
        return list3

    def appendToList(myList, newValue):
        myList.append(newValue)
        return myList

    def sliceList(myList, start, end):
        """
        Just like strings, you can slice LISTS as well,
        Start will mark where the return list will start
        if empty, it will start at the beginning
        End will mark where the list will end, not including the end position

        """
        return myList[start:end]

    def setMultipleNumbers(myList, newValue1, newValue2):
        """
        We can add multiple itens to lists by slicing an interval on that list
        and attributing a new list to overwrite the old values
        It can also work to add a new, bigger list into the first list position

                EX:
                list1 = [1,2,3,4,5]

                list1[0:2] prints the list [1,2]
                if I set a new list to that exact position,
                it will overwrite the values

                list1[0:2] = [9,9]

                list1 will print [9,9,3,4,5]

        It can also work to add a new, bigger list into the first list position

                EX:

                list1 = [1,2,3]

                list1[0:2] = [9,9,9,9,9,9,9,9]

                It will overwrite the first two values,
                and add the remaining ones
                list1 will print [9,9,9,9,9,9,9,9,3]


        """
        myList[0:2] = [newValue1, newValue2]
        return myList

    def deleteFromList(myList, position, start, end):
        if not start or not end:
            myList[position] = []
        else:
            myList[start:end] = []
        return myList

    def deleteEntireList(myList):
        myList[:] = []
        return myList
