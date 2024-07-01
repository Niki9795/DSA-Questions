class BubbleSort():

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def bubbleSort(self):
        swapped = False
        for i in range(self.length - 1):
            for j in range(1, self.length - i):
                if self.array[j - 1] > self.array[j]:
                    temp = self.array[j - 1]
                    self.array[j - 1] = self.array[j]
                    self.array[j] = temp
                    j += 1
                    swapped = True
            i += 1

            if not swapped:
                break 
        return self.array
    
array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
bubble = BubbleSort(array)
print(bubble.bubbleSort())