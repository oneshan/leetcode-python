# 0198 - House Robber
# Date: 2024-02-12
# Runtime: 34 ms, Memory: 16.5 MB
# Submission Id: 1172708461


class Solution:
    def rob(self, nums: List[int]) -> int:
        p1 = p2 = 0
        for num in nums:
            p2, p1 = p1, max(p1, p2 + num)
        return p1