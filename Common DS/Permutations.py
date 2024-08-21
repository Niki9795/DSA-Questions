class Permutations():

    def permutations(self, processedString, unProcessedString):
        result = []
        if unProcessedString == "":
            result.append(processedString)
            return result
        
        ch = unProcessedString[0]
        for i in range(len(processedString) + 1):
            first = processedString[0:i]
            second = processedString[i:len(processedString)]
            result.extend(self.permutations(first + ch + second, unProcessedString[1:]))

        return result

string = input("Enter a string\n")
permutations = Permutations()
answer = permutations.permutations("", string)
print("Possible Permutations are:", answer)