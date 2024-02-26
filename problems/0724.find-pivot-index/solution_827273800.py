# 0724 - Find Pivot Index
# Date: 2022-10-21
# Runtime: 153 ms, Memory: 15.2 MB
# Submission Id: 827273800


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        for idx, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return idx
            left_sum += num
        return -1