class Solution:
    def __init__(self, n):
        self.n = n
        self.stack = []
        self.result = []

    def generateParenthesis(self):
        def backtracking(open, close):
            if open == close == self.n:
                self.result.append("".join(self.stack))
                return

            if open < self.n:
                self.stack.append("(")
                backtracking(open + 1, close)
                self.stack.pop()

            if close < open:
                self.stack.append(")")
                backtracking(open, close + 1)
                self.stack.pop()
        
        backtracking(0,0)
        return self.result
    
solution = Solution(3)
print(solution.generateParenthesis())
