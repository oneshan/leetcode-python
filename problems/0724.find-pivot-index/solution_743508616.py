# 0724 - Find Pivot Index
# Date: 2022-07-10
# Runtime: 299 ms, Memory: 15.2 MB
# Submission Id: 743508616


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        for idx in range(len(nums)):
            right_sum -= nums[idx]
            if left_sum == right_sum:
                return idx
            left_sum += nums[idx]
        return -1