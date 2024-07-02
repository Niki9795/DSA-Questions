class Solution():

    def intersect(self, nums1, nums2):
        result = []
        count1 = {}
        
        for num in nums1:
            if num in count1:
                count1[num] += 1
            else:
                count1[num] = 1
        
        for num in nums2:
            if num in count1 and count1[num] > 0:
                result.append(num)
                count1[num] -= 1
        
        return result
solution = Solution()
print(solution.intersect([1,2,2,1], [2,2]))