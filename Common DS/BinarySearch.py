"""
Binary Search on 1D array
"""
class BinarySearch1D():

    def __init__(self, array, target):
        self.array = sorted(self.array)
        print("Sorted array is:", self.array)
        self.target = target
        
    def binarySearch1D(self):
        start = 0
        end = len(self.array) - 1
        
        while start <= end:
            middle = int((start + (end - start) / 2))

            if self.target < self.array[middle]:
                end = middle - 1
            elif self.target > self.array[middle]:
                start = middle + 1
            else:
                print(f"Target found at index {middle} in the given array")
                return middle

        print("Target does not found in the given array")   
        return -1
    
array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
target = int(input("Enter an element to search in an array\n"))
binarysearch1D = BinarySearch1D(array, target)
binarysearch1D.binarySearch1D()

"""
Binary Search on 2D array
"""
class BinarySearch2D():

    def __init__(self, array, target):
        self.array = array
        self.target = target

    def binarySearch2D(self):

        for i in range(len(self.array)):
            for j in range(len(self.array)):
                if self.array[i][j] == self.target:
                    return f"Target found in given array at index array[{i},{j}]"
        return f"Target does not found in given array"

# Taking input for a 2D array
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter elements of the array row-wise, separated by commas:")

array = []
for _ in range(rows):
    row = [int(n) for n in input().split(",") if n.strip()]
    array.append(row)

target = int(input("Enter an element to search in the array: "))

binarysearch2D = BinarySearch2D(array, target)
print(binarysearch2D.binarySearch2D())