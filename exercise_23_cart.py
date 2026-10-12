class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        self.items.pop(name)

    def count(self):
        return len(self.items)

    def total(self):
        return sum(self.items.values())

cart = ShoppingCart()
cart.add_item("backpack", 29.99)
cart.add_item("bike light", 9.99)
cart.add_item("t-shirt", 15.99)

print(cart.count())
print(round(cart.total(), 2))

cart.remove_item("bike light")

print(cart.count())
print(round(cart.total(), 2))