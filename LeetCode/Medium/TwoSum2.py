class Solution():

    def twoSum(self, numbers, target):

        start = 0
        end = len(numbers) - 1

        while start <= end:

            if numbers[start] + numbers[end] == target:
                return [start  + 1, end + 1]
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1

        return [-1, -1]
    
solution = Solution()
print(solution.twoSum([3,24,50,79,88,150,345], 200))
