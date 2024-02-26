# 1514 - Minimum Value to Get Positive Step by Step Sum
# Date: 2022-10-14
# Runtime: 54 ms, Memory: 13.8 MB
# Submission Id: 822302894


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = prefix_sum = 0
        for num in nums:
            prefix_sum += num
            min_val = min(min_val, prefix_sum)
        return -min_val + 1