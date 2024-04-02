class BinarySearch():

    def __init__(self, array, target):
        self.array = sorted(self.array)
        print("Sorted array is:", self.array)
        self.target = target
        
    def binarySearch(self):
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
binarysearch = BinarySearch(array, target)
binarysearch.binarySearch()
