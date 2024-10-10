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
        str = ""
        for i in self.allItems:
            str += f"{i}, "
        print(str)

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

example = [3, 4]
example_item = myList([8, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 7])
example_item.print_items_clean()
example_item.reverse_items()
example_item.print_items_clean()
example_item.sort_items()
example_item.print_items_clean()


# example.reverse()


