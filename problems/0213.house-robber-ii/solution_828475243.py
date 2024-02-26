# 0213 - House Robber II
# Date: 2022-10-23
# Runtime: 67 ms, Memory: 13.9 MB
# Submission Id: 828475243


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        ans = 0
        
        p2 = p1 = 0
        for i in range(n-1):
            p2, p1 = p1, max(p2+nums[i], p1)
        ans = p1
        
        p2 = p1 = 0
        for i in range(1, n):
            p2, p1 = p1, max(p2+nums[i], p1)
        
        ans = max(ans, p1)
        return ans