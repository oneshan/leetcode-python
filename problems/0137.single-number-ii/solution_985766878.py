# 0137 - Single Number II
# Date: 2023-07-04
# Runtime: 79 ms, Memory: 17.9 MB
# Submission Id: 985766878


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = two = 0
        for num in nums:
            one = (one ^ num) & (~two)
            two = (two ^ num) & (~one)
        return one