class Factorial():

    def __init__(self):
        self.result = 1

    def factorial(self, digit):
        if digit == 0:
            return self.result
        return digit * self.factorial(digit - 1)

factorial = Factorial()

digit = int(input("Enter the digit for which you want facorial:"))
print(factorial.factorial(digit))