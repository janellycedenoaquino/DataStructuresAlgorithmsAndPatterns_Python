class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations for args
        assert price >= 0, f"Price of {price} is not greater than zero"
        assert quantity >= 0, f"Quantity of {quantity} is not greater than zero"

        # Assign values
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 1, 5)
item1 = Item("Laptop", 1, 5)


