# 1993 - Sum of All Subset XOR Totals
# Date: 2024-05-20
# Runtime: 98 ms, Memory: 16.5 MB
# Submission Id: 1262804253


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range((1 << n)):
            curr = 0
            for j in range(n):
                if (1 << j) & i:
                    curr ^= nums[j]
            ans += curr
        return ans