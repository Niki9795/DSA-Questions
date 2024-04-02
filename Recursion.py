"""
Factorial using Recursion
"""
class Factorial():

    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n-1)
    
factorial = Factorial()
n = int(input("Enter the value for which you'd like to compute the factorial:\n"))
print(f"Factorial of {n} is {factorial.factorial(n)}")

"""
Sum of digits using Recusion
"""
class Sum():
    
    def sum(self, n):
        if n == 0:
            return 0
        return (n % 10) + self.sum(n // 10)
    
sum = Sum()
n = int(input("Enter the digit you want to get sum of\n"))
print(f"Sum of the digit {n} is {sum.sum(n)}")

"""
Reverse a number using Recursion
"""
class Reverse():

    def __init__(self):
        self.sum = 0
        self.remainder = 0 

    def reverse(self, n):
        if n == 0:
            return self.sum
        
        self.remainder = n % 10
        self.sum = (self.sum * 10) + self.remainder
        return self.reverse(n // 10)
    
reverse = Reverse()
n = int(input("Enter a number you want to reverse\n"))
print(f"Reverse of a {n} is {reverse.reverse(n)}")

"""
Fibonacci Number using Recursion
"""
class Fibonacci():
    
    def fibonacci(self, n):
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

test = Fibonacci()
n = int(input("Enter the index for Fibonacci Number:\n"))
fibonacciNumber = test.fibonacci(n)
print(f"Fibonacci Number at index {n} is {fibonacciNumber}")

"""
Binary Search using Recursion
"""
class BinarySearch():
    def __init__(self, array, target):
        self.target = target
        self.array = sorted(self.array)
        print("Sorted array is:", self.array)

    def binarySearch(self, start, end):
        if start <= end:

            middle = start + ((end - start) // 2)

            if self.target < self.array[middle]:
                self.binarySearch(start, middle - 1)
            elif self.target > self.array[middle]:
                self.binarySearch(middle + 1, end)
            else:
                print(f"Target found at index {middle} in the given array")
                return middle
        else:
            print(f"Target does not found in given array")
            return -1
    
array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
target = int(input("Enter an element to search in an array\n"))
binarysearch = BinarySearch(array, target)
binarysearch.binarySearch(0, len(array) - 1)