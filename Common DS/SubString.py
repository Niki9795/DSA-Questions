"""
Finding sub string of a string using Recursion
"""
class SubString():

    def subString(self, processedString, unPrpcessedString):
        result = []
        if unPrpcessedString == "":
            result.append(processedString)
            return result
        
        ch = unPrpcessedString[0]

        left = self.subString(processedString + ch, unPrpcessedString[1:])
        right = self.subString(processedString, unPrpcessedString[1:])

        return left + right

string = input("Enter a string\n")
subString = SubString()
print("Possible Sub Strings are:", subString.subString("", string))

"""
Finding sub string of a string using Iteration
"""
class SubString():

    def subString(self, array):
        outerResult = [[]]

        for ch in array:
            arraySize = len(outerResult)
            for i in range(arraySize):
                innerResult = [] + outerResult[i]
                innerResult.append(ch)
                outerResult.append(innerResult)
        return outerResult
    
array = [str(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
subString = SubString()
print("Possible Sub Strings are:", subString.subString(array))

"""
Finding sub string of a string of duplicate elements using Iteration
"""
class SubString():
    
    def subString(self, array):
        outerResult = [[]]

        start = 0
        end = 0
        for i in range(len(array)):
            if i > 0 and array[i] == array[i - 1]:
                start = end + 1
            end = len(outerResult) - 1
            arraySize = len(outerResult)
            for j in range(start, arraySize):
                innerResult = [] + outerResult[j]
                innerResult.append(array[i])
                outerResult.append(innerResult)

        return outerResult
    
array = [str(n) for n in input("Enter the elements of an array seperated by comma\n").split(",") if n.strip()]
subString = SubString()
print("Possible Sub Strings are:", subString.subString(sorted(array)))
