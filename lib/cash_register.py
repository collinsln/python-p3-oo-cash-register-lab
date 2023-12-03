class CashRegister:
    def __init__(self):
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0  # To keep track of the last transaction amount

    def add_item(self, item_name, price, quantity=1):
        # Add the item(s) to the register and update total
        self.last_transaction_amount = price * quantity
        self.total += self.last_transaction_amount
        for _ in range(quantity):
            self.items.append(item_name)

    def calculate_discount(self, discount_percentage):
        # Apply discount to the total based on the given percentage
        discount = (discount_percentage / 100) * self.total
        self.total -= discount

    def void_last_transaction(self):
        # Remove the last transaction from the total
        self.total -= self.last_transaction_amount
        # Remove the last item(s) added
        for _ in range(self.items.count()):
            self.items.pop()

    # Add any additional methods required as per specifications
