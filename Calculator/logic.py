class Calculator():
    def __init__(self):
        self.total = 0
        self.last_total = 0
    
    def add(self,number):
        self.last_total = self.total
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
        try:
            self.last_total = self.total
            self.total /= number
            return self.total
        except ZeroDivisionError:
            print("Cannot divide by Zero")
        



