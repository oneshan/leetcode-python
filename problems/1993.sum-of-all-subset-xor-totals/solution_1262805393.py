# 1993 - Sum of All Subset XOR Totals
# Date: 2024-05-20
# Runtime: 55 ms, Memory: 16.6 MB
# Submission Id: 1262805393


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        n = len(nums)

        def recur(i, curr):
            self.ans += curr
            for j in range(i, n):
                curr ^= nums[j]
                recur(j+1, curr)
                curr ^= nums[j]

        recur(0, 0)
        return self.ans