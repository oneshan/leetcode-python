# 1993 - Sum of All Subset XOR Totals
# Date: 2024-05-20
# Runtime: 38 ms, Memory: 16.5 MB
# Submission Id: 1262810148


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans |= num
        return ans << (len(nums)-1)