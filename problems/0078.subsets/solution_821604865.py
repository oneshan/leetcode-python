# 0078 - Subsets
# Date: 2022-10-13
# Runtime: 42 ms, Memory: 14.1 MB
# Submission Id: 821604865


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)
        
        for mask in range(2**n):
            ans.append([nums[i] for i in range(n) if mask & (1<<i)])
        
        return ans