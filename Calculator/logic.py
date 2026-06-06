class Calculator():
    def __init__(self):
        self.total = None
        self.last_total = 0
    
    def add(self,number):
        self.last_total = self.total
        if self.total is None:
             self.total = number
        else:    
            self.total += number
        return self.total

    def subtract(self,number):
        self.last_total = self.total
        self.total -= number
        return self.total
    
    def multiply(self,number):
        self.last_total = self.total
        self.total *= number
        return self.total

    def divide(self,number):
            self.last_total = self.total
            self.total /= number
            return self.total
        



