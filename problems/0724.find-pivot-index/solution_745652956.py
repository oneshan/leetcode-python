# 0724 - Find Pivot Index
# Date: 2022-07-13
# Runtime: 230 ms, Memory: 15.2 MB
# Submission Id: 745652956


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        for idx, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return idx
            left_sum += num
        return -1