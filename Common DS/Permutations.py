"""
Permutation using Recursion
"""
class Permutations():

    def permutations(self, processedString, unPrpcessedString):
        result = []
        if unPrpcessedString == "":
            result.append(processedString)
            return result
        
        ch = unPrpcessedString[0]

        left = self.permutations(processedString + ch, unPrpcessedString[1:])
        right = self.permutations(processedString, unPrpcessedString[1:])

        return left + right

string = input("Enter a string\n")
permutations = Permutations()
print("Possible Permutations are:", permutations.permutations("", string))

"""
Permutation using Iteration
"""
class Permutations():

    def permutations(self, array):
        outerResult = [[]]

        for ch in array:
            arraySize = len(outerResult)
            for i in range(arraySize):
                innerResult = [] + outerResult[i]
                innerResult.append(ch)
                outerResult.append(innerResult)
        return outerResult
    
array = [str(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
permutations = Permutations()
print("Possible Permutations are:", permutations.permutations(array))