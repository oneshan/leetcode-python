# 0213 - House Robber II
# Date: 2024-05-21
# Runtime: 36 ms, Memory: 16.4 MB
# Submission Id: 1263802062


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def check(left, right):
            p2 = p1 = 0
            for i in range(left, right):
                p2, p1 = p1, max(p1, p2+nums[i])
            return p1

        return max(check(0, n-1), check(1, n))