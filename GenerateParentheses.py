class Solution:
    def __init__(self, n):
        self.n = n
        self.stack = []
        self.result = []

    def generateParenthesis(self):
        def backtracking(openN, closeN):
            if openN == closeN == self.n:
                self.result.append("".join(self.stack))
                return

            if openN < self.n:
                self.stack.append("(")
                backtracking(openN + 1, closeN)
                self.stack.pop()

            if closeN < openN:
                self.stack.append(")")
                backtracking(openN, closeN + 1)
                self.stack.pop()
        
        backtracking(0,0)
        return self.result
    
solution = Solution(3)
print(solution.generateParenthesis())
