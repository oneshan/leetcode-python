# 1514 - Minimum Value to Get Positive Step by Step Sum
# Date: 2022-10-14
# Runtime: 74 ms, Memory: 13.9 MB
# Submission Id: 822335599


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = start = 0
        for num in nums:
            prefix_sum += num
            start = min(start, prefix_sum)
        return -start + 1