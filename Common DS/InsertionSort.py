class InsertionSort():

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def insertionSort(self):
        for i in range(self.length - 1):
            for j in range(i + 1, 0, -1):
                if self.array[j] < self.array[j - 1]:
                    temp = self.array[j]
                    self.array[j] = self.array[j - 1]
                    self.array[j - 1] = temp
                else:
                    break
        return self.array
    
array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
insertion = InsertionSort(array)
print(insertion.insertionSort())