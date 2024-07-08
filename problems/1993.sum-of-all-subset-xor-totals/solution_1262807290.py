# 1993 - Sum of All Subset XOR Totals
# Date: 2024-05-20
# Runtime: 49 ms, Memory: 16.6 MB
# Submission Id: 1262807290


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        def recur(i, curr):
            if i == n:
                return curr
            return (recur(i+1, curr) + recur(i+1, curr ^ nums[i]))

        return recur(0, 0)