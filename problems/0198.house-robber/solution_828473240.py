# 0198 - House Robber
# Date: 2022-10-23
# Runtime: 57 ms, Memory: 13.9 MB
# Submission Id: 828473240


class Solution:
    def rob(self, nums: List[int]) -> int:
        p2 = p1 = 0
        for num in nums:
            p2, p1 = p1, max(p2+num, p1)
        return p1