class Solution():

    def numIdenticalPairs(self, nums):
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
    
solution = Solution()
print(solution.numIdenticalPairs([1,1,1,1]))