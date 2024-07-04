class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        delta = (bobSum - aliceSum) // 2  # The amount Bob needs to give to Alice to balance the candy.
        
        bobSet = set(bobSizes)  # Convert Bob's list to a set for O(1) lookups.
        
        for a in aliceSizes:
            b = a + delta  # Find the candy size Bob needs to give to Alice.
            if b in bobSet:
                return [a, b]  # Return the pair as soon as a valid swap is found.

# Example usage
solution = Solution()
print(solution.fairCandySwap([1, 1], [2, 2]))