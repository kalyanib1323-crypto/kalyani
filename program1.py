class Calculator:
    def __init__(self, a: int, b: int, operation: str):
        self.A = A
        self.B = B
        self.operation = operation

    def cal(self):
        if self.operation == "Addition":
            return self.A + self.B
        elif self.operation == "Subtraction":
            return self.A - self.B
        elif self.operation == "Multiplication":
            return self.A * self.B
        elif self.operation == "Division":
            if self.b != 0:
                return self.A / self.B
            else:
                return "Error:Division By Zero"
        else:
            return "Error:Invalid Operation"


# 
A = int(input("Enter First Number: "))
B = int(input("Enter Second Number: "))
operation = input("Enter Operation (Addition, Subtraction, Multiplication, Division): ")

calc = Calculator(A, B, operation)
result = calc.cal()

print("Result:", result)