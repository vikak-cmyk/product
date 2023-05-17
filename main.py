class ShoppingCart(object):

    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        self.total += (quantity * price)
        self.items = {item_name: quantity}

    def remove_item(self, item_name, quantity, price):
        self.total -= (quantity * price)
        if quantity > self.items[item_name]:
            del self.items[item_name]
        self.items[item_name] -= quantity

    def checkout(self, cash_paid):
        if cash_paid < self.total:
            return "Cash paid not enough"
        balance = cash_paid - self.total
        return balance


class Shop(ShoppingCart):

    def __init__(self):
        ShoppingCart.__init__(self)
        self.quantity = 100

    def remove_item(self, **kwargs):
        self.quantity -= 1
