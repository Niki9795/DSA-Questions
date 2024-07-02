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