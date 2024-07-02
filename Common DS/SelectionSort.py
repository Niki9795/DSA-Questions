class SelectionSort:

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def selectionSort(self):
        for i in range(self.length):
            lastIndex = self.length - i - 1
            maxIndex = self.getMaxIndex(0, lastIndex)
            temp = self.array[maxIndex]
            self.array[maxIndex] = self.array[lastIndex]
            self.array[lastIndex] = temp
        return self.array

    def getMaxIndex(self, startIndex, endIndex):
        maxIndex = startIndex
        for i in range(startIndex, endIndex + 1):
            if self.array[i] > self.array[maxIndex]:
                maxIndex = i
        return maxIndex

array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
selectionSort = SelectionSort(array)
print(selectionSort.selectionSort())