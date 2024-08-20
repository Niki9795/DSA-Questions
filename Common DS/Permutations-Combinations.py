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