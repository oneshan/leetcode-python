# 0198 - House Robber
# Date: 2024-01-21
# Runtime: 34 ms, Memory: 16.7 MB
# Submission Id: 1152117222


class Solution:
    def rob(self, nums: List[int]) -> int:
        p2 = p1 = 0
        for num in nums:
            p2, p1 = p1, max(p2+num, p1)
        return p1