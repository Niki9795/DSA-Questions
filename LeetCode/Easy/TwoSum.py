"""
Brute Force Way
"""

class TwoSumBruteForce():

    def __init__(self, array, tagret):
        self.array = array
        self.target = tagret

    def twoSumBruteForce(self):
        for i in range(len(self.array)):
            for j in range(1, len(self.array)):
                result = self.array[i] + self.array[j]

                if result == self.target:
                    return [i, j]
                
array = [int(element) for element in input("Eneter elements seperated by coma: ").split(",") if element.strip()]
target = int(input("Enter the target element: "))

twosumbruteforce = TwoSumBruteForce(array, target)
print("The indexs of that elements are: ",twosumbruteforce.twoSumBruteForce())

"""
Using Hash Table
"""

class TwoSumHashTable():

    def __init__(self, array, target):
        self.array = array
        self.target = target
        self.dictionary = {}

    def twoSumHashTable(self):
        for i in range(len(self.array)):
            diff = self.target - self.array[i]
            if diff in self.dictionary:
                return [self.dictionary[diff], i]
            
            self.dictionary[self.array[i]] = i

array = [int(element) for element in input("Eneter elements seperated by coma: ").split(",") if element.strip()]
target = int(input("Enter the target element: "))

twosumhashtable = TwoSumHashTable(array, target)
print("The indexs of that elements are: ",twosumhashtable.twoSumHashTable())