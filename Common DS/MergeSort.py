"""
Merge Sort in Place Technique
"""
class MergeSort():

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def merge(self, start, mid, end):
        mix = [0] * (end - start)

        ptr1 = start
        ptr2 = mid
        mixArrayPtrr = 0

        while ptr1 < mid and ptr2 < end:
            if self.array[ptr1] < self.array[ptr2]:
                mix[mixArrayPtrr] = self.array[ptr1]
                ptr1 += 1
            else:
                mix[mixArrayPtrr] = self.array[ptr2]
                ptr2 += 1
            mixArrayPtrr += 1

        while ptr1  < mid:
            mix[mixArrayPtrr] = self.array[ptr1]
            ptr1 += 1
            mixArrayPtrr += 1

        while ptr2 < end:
            mix[mixArrayPtrr] = self.array [ptr2]
            ptr2 += 1
            mixArrayPtrr += 1 

        for i in range(0, len(mix)):
            self.array[start + i] = mix[i]

    def sort(self, start, end):
        if end - start <= 1:
            return
        
        mid = start + (end - start) // 2

        self.sort(start, mid)
        self.sort(mid, end)

        self.merge(start, mid, end)

    def get_sorted_array(self):
        return self.array
    
array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
mergesort = MergeSort(array)
sortedArray = mergesort.sort(0, mergesort.length)
sortedArray = mergesort.get_sorted_array()
print("Sorted array:", sortedArray)

"""
Merge Sort by taking copy of array technique
"""
class MergeSort():

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def merge(self, left, right):
        mix = [0] * (len(left) + len(right))

        ptr1 = 0
        ptr2 = 0
        mixArrayPtrr = 0

        while ptr1 < len(left) and ptr2 < len(right):
            if left[ptr1] < right[ptr2]:
                mix[mixArrayPtrr] = left[ptr1]
                ptr1 += 1
            else:
                mix[mixArrayPtrr] = right[ptr2]
                ptr2 += 1
            mixArrayPtrr += 1

        while ptr1  < len(left):
            mix[mixArrayPtrr] = left[ptr1]
            ptr1 += 1
            mixArrayPtrr += 1

        while ptr2 < len(right):
            mix[mixArrayPtrr] = right[ptr2]
            ptr2 += 1
            mixArrayPtrr += 1 

        return mix

    def sort(self, array=None):
        if array is None:
            array = self.array

        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left = self.sort(array[:mid])
        right = self.sort(array[mid:])

        return self.merge(left, right)
    
array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
mergesort = MergeSort(array)
sortedArray = mergesort.sort()
print("Sorted array is:", sortedArray)