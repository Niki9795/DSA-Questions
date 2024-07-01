# """
# Factorial using Recursion
# """
# class Factorial():

#     def factorial(self, n):
#         if n == 0:
#             return 1
#         return n * self.factorial(n-1)
    
# factorial = Factorial()
# n = int(input("Enter the value for which you'd like to compute the factorial:\n"))
# print(f"Factorial of {n} is {factorial.factorial(n)}")

# """
# Sum of digits using Recusion
# """
# class Sum():
    
#     def sum(self, n):
#         if n == 0:
#             return 0
#         return (n % 10) + self.sum(n // 10)
    
# sum = Sum()
# n = int(input("Enter the digit you want to get sum of\n"))
# print(f"Sum of the digit {n} is {sum.sum(n)}")

# """
# Reverse a number using Recursion
# """
# class Reverse():

#     def __init__(self):
#         self.sum = 0
#         self.remainder = 0 

#     def reverse(self, n):
#         if n == 0:
#             return self.sum
        
#         self.remainder = n % 10
#         self.sum = (self.sum * 10) + self.remainder
#         return self.reverse(n // 10)
    
# reverse = Reverse()
# n = int(input("Enter a number you want to reverse\n"))
# print(f"Reverse of a {n} is {reverse.reverse(n)}")

# """
# Fibonacci Number using Recursion
# """
# class Fibonacci():
    
#     def fibonacci(self, n):
#         if n <= 1:
#             return n
#         return self.fibonacci(n - 1) + self.fibonacci(n - 2)

# test = Fibonacci()
# n = int(input("Enter the index for Fibonacci Number:\n"))
# fibonacciNumber = test.fibonacci(n)
# print(f"Fibonacci Number at index {n} is {fibonacciNumber}")

# """
# Binary Search using Recursion
# """
# class BinarySearch():
#     def __init__(self, array, target):
#         self.target = target
#         self.array = sorted(self.array)
#         print("Sorted array is:", self.array)

#     def binarySearch(self, start, end):
#         if start <= end:

#             middle = start + ((end - start) // 2)

#             if self.target < self.array[middle]:
#                 self.binarySearch(start, middle - 1)
#             elif self.target > self.array[middle]:
#                 self.binarySearch(middle + 1, end)
#             else:
#                 print(f"Target found at index {middle} in the given array")
#                 return middle
#         else:
#             print(f"Target does not found in given array")
#             return -1
    
# array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
# target = int(input("Enter an element to search in an array\n"))
# binarysearch = BinarySearch(array, target)
# binarysearch.binarySearch(0, len(array) - 1)

# """
# Array is sorted or not using Recursion
# """
# class Sorted():

#     def sorted(self, array, index):
#         if index == len(array) - 1:
#             print("Given array is sorted")
#             return

#         if array[index] < array[index + 1]:
#             self.sorted(array, index + 1)
#             return
#         else:
#             print("Given array is not sorted")

# array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
# sorted = Sorted()
# sorted.sorted(array, 0)

# """
# Linear Search using Recursion
# """
# class LinearSearch():

#     def __init__(self, target):
#         self.target = target
#         self.targetList = []

#     def linearSearch(self, array, index):
#         if index == len(array):
#             if not self.targetList:
#                 print("Target not found in the given array")
#             return self.targetList

#         if self.target == array[index]:
#             self.targetList.append(index)
#             print(f"Target found at index {index} in given array")
        
#         return self.linearSearch(array, index + 1)
        
# array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
# target = int(input("Enter an element to search in an array\n"))
# linearsearch = LinearSearch(target)
# print("Indexes where the target is found:", linearsearch.linearSearch(array, 0))

# """
# Pattern Printing using Recursion
# """
# class Pattern():

#     def pattern(self, r, c):

#         if r == 0:
#             return
        
#         if c < r:
#             print("*", end = "")
#             self.pattern(r, c + 1)
#         else:
#             print()
#             self.pattern(r - 1, 0)

# pattern = Pattern()
# rows = int(input("Enter the number of rows for pattern\n"))

# pattern.pattern(rows, 0)

"""
Bubble Sort using Recursion
"""     

class BubbleSort():

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def bubbleSort(self, i, j):
        if i == self.length - 1:
            return self.array
        
        if i < self.length - 1:
            if j < self.length - i - 1:
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                return self.bubbleSort(i, j + 1)
            return self.bubbleSort(i + 1, 0)
            
        return self.array
    
array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
bubble = BubbleSort(array)
print(bubble.bubbleSort(0, 0))