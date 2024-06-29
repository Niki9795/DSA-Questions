class CyclicSort():

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def cyclicsort(self):
        i = 0
        while i < self.length:
            element = self.array[i]
            correctIndex = element - 1

            if i == correctIndex or self.array[i] == self.length:
                i += 1
            else:            
                temp = self.array[i]
                self.array[i] = self.array[correctIndex]
                self.array[correctIndex] = temp

        return self.array
    
array = [int(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
cycle = CyclicSort(array)
print(cycle.cyclicsort())