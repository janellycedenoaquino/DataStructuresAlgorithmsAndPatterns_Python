class MyObject:
    obj = {}

    def __init__(self, object):
        for key, value in object.items():
            self.obj[key] = value

    def pop_item_(self, item):
        removedItem = self.obj[item]
        del self.obj[item]

    def pop_last_items_(self):
        last_key = ""
        for key in self.obj:
            last_key = key
        del self.obj[last_key]

    def item_values(self):
        listOfValues = []
        for values in self.obj.values():
            listOfValues.append(values)
        return listOfValues

    def item_keys(self):
        listOfKeys = []
        for keys in self.obj.keys():
            listOfKeys.append(keys)
        return

    def Obj_Items(self):
        obj_items = []
        for key in self.obj:
            obj_items.append(tuple([key, self.obj[key]]))
        return f"obj_items({obj_items})"
