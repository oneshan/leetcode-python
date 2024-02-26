# 1514 - Minimum Value to Get Positive Step by Step Sum
# Date: 2023-08-15
# Runtime: 38 ms, Memory: 16.2 MB
# Submission Id: 1022154284


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = start = 0
        for num in nums:
            prefix_sum += num
            start = min(start, prefix_sum)
        return -start + 1