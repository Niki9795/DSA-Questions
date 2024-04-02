from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for s in strs:
            length = len(s)
            string += str(length) + '+' + s 
        return string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '+':
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return result
                
    

input = ["neet","code","love","you"]

solution = Solution()
encode = solution.encode(input)
print(encode)
decode = solution.decode(encode)
print(decode)

