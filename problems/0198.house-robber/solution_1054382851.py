# 0198 - House Robber
# Date: 2023-09-20
# Runtime: 27 ms, Memory: 16.2 MB
# Submission Id: 1054382851


class Solution:
    def rob(self, nums: List[int]) -> int:
        p2 = p1 = 0
        for num in nums:
            p2, p1 = p1, max(p1, p2 + num)
        return max(p2, p1)