class Anagrams():

    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def validAnagrams(self):
        self.string1 = sorted(self.string1)
        self.string2 = sorted(self.string2)

        if self.string1 == self.string2:
            return f"Strings are anagrams"
        return f"Strings are not anagrams"
    
string1 = input("Enter string1: ")
string2 = input("Enter string2: ")
    
anagrams = Anagrams(string1, string2)
print(anagrams.validAnagrams())