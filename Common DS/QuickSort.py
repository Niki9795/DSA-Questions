class QuickSort:

    def __init__(self, array):
        self.array = array
        self.length = len(self.array)

    def sort(self, low, high):
        start = low
        end = high
        mid = start + (end - start) // 2
        pivot = self.array[mid]
        
        if low >= high:
            return
        
        while start <= end:
            while self.array[start] < pivot:
                start += 1
            while self.array[end] > pivot:
                end -= 1
            if start <= end:
                self.array[start], self.array[end] = self.array[end], self.array[start]
                start += 1
                end -= 1
        
        self.sort(low, end)
        self.sort(start, high)
        return self.array
    
array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
quickSort = QuickSort(array)
sortedArray = quickSort.sort(0, quickSort.length - 1)
print("Sorted array:", sortedArray)


