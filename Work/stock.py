class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.price = price
        self.shares = shares

    def cost(self):
        return self.price*self.shares
    
    def sell(self, sold):
        self.shares -= sold
        return self.price*self.shares