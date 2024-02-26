# 1692 - Number of Ways to Reorder Array to Get Same BST
# Date: 2023-06-17
# Runtime: 180 ms, Memory: 21.9 MB
# Submission Id: 972729814


from math import comb

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        
        def dfs(nums):
            m = len(nums)
            if m < 3:
                return 1
            left = [a for a in nums if a < nums[0]]
            right = [a for a in nums if a > nums[0]]
            return dfs(left) * dfs(right) * comb(m-1, len(left)) % mod
        
        return (dfs(nums) - 1) % mod