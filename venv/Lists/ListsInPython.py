class myList:

    allItems = []

    def __init__(self, listOfItems):
        for item in listOfItems:
            self.allItems.append(item)

    def append_item(self, newItem):
        self.allItems.append(newItem)

    def remove_item(self, item):
        for i in self.allItems:
            if i == item:
                self.allItems.remove(i)

    def pop_item(self):
        last_item = self.allItems[-1]
        self.allItems.remove(self.allItems[-1])
        return last_item

    def clear_items(self):
        self.allItems.clear()

    def print_items(self):
        idx = 0
        for item in self.allItems:
            print(f"item at index {idx} is {item}")
            idx += 1

    def print_items_clean(self):
        str_r = ", ".join(str(i) for i in self.allItems)
        print(str_r)

    def reverse_items(self):
        left = 0
        right = len(self.allItems) - 1
        while left <= right:
            left_val = self.allItems[left]
            self.allItems[left] = self.allItems[right]
            self.allItems[right] = left_val
            left += 1
            right -= 1

    def sort_items(self):
        self.allItems.sort()


"""
given a row and column wise (nxn) sorted matrix.
write a program to search a key in a given matrix 
ex: 
            0   1   2   3
        0  10  20  30  40
        1  15  25  35  45
        2  27  29  37  48
        3  32  33  39  51
            matrix[][]
        
        x = 32 n = 4   
        search(matrix, 4, 32 
        
        4x4 matrix
        x is the key 
        
        
        """


def searchMatrix(matrix, n, x):
    if matrix is None:
        return 0

    i = 0
    j = n - 1
    while i < n and j >= 0:
        if matrix[i][j] == x:
            return "Matrix["+str(i)+"]["+str(j)+"]"

        if matrix[i][j] > x:
            j -= 1
        else:
            i += 1
    return "no such value"


example = [3, 4]
example_item = myList([8, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 7])
matrix1 = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 51]]
# example_item.print_items_clean()
# example_item.reverse_items()
# example_item.print_items_clean()
# example_item.sort_items()
# example_item.print_items_clean()


# example.reverse()


