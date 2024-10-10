class MyTuple:

    allElements = []

    def __init__(self, elements):
        self.allElements = elements
        self.allElements = tuple(self.allElements)

    def index_element(self, idx):
        return self.allElements[idx]

    def count_element(self, element):
        count = 0
        for item in self.allElements:
            if element == item:
                count += 1
        return count


newTuple = MyTuple([1, 2, 3, 3, 3, 3, 4, 5])
actualTuple = (1, 2, 3, 4, 5)


print(actualTuple.count(3))
print(newTuple.count_element(3))

