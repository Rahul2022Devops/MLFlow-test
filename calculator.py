class calculator:
    def __init__(self):
        self.num1 = int(input("Enter the first number"))
        self.num2 = int(input("Enter the second number"))
    def add(self):
        r = self.num1 + self.num2
        reasult = f"The sum of {self.num1} and {self.num2} is {r}"
        print(reasult)
    def substract(self):
        r = self.num1 - self.num2
        reasult = f"The substract of {self.num1} and {self.num2} is {r}"
        print(reasult)
    def multiply(self):
        r = self.num1 * self.num2
        reasult = f"The multiply of {self.num1} and {self.num2} is {r}"
        print(reasult)
    def divide(self):
        r = self.num1 / self.num2
        reasult = f"The divide of {self.num1} and {self.num2} is {r}"
        print(reasult)

if __name__ == "__main__":
    cal = calculator()
    cal.add()
    cal.substract()
    cal.multiply()
    cal.divide()

