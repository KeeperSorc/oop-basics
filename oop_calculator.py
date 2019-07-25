class Calculator:
    def __init__(self,number1=5,number2=12):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return float(self.number1/self.number2)

    def circle_area(self,radius):
        return 3.14*(radius**2)