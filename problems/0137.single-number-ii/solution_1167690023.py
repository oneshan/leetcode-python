# 0137 - Single Number II
# Date: 2024-02-06
# Runtime: 61 ms, Memory: 18.5 MB
# Submission Id: 1167690023


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = two = 0
        for num in nums:
            one = (one ^ num) & (~two)
            two = (two ^ num) & (~one)
        return one