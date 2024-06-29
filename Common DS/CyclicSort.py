class CyclicSort():

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def cyclicsort(self):
        missingNumber = 0
        i = 0
        while i < self.length:
            element = self.array[i]
            correctIndex = element 

            if i == correctIndex or self.array[i] == self.length:
                print("Step = ",i, self.array)
                i += 1
            else:            
                temp = self.array[i]
                self.array[i] = self.array[correctIndex]
                self.array[correctIndex] = temp

            print("Step = ",i, self.array)
        for i in range(self.length):
            if self.array[i] != i:
                missingNumber = i
                break
            else:
                missingNumber = self.length
        return missingNumber
    
array = [9,6,4,2,3,5,7,0,1]
cycle = CyclicSort(array)
print(cycle.cyclicsort())