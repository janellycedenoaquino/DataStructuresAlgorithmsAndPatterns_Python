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

newList = myList(["a", "b", "c", 1, 2, 3])
newList.print_items_clean()
# newList.append_item(7)
# newList.print_items_clean()
# newList.remove_item("b")
# newList.print_items_clean()
# poppedItem = newList.pop_item()
# newList.print_items_clean()
newList.clear_items()
# print(poppedItem)
print("after clear: ")
newList.print_items_clean()


