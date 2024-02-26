# 0724 - Find Pivot Index
# Date: 2022-07-10
# Runtime: 200 ms, Memory: 15.2 MB
# Submission Id: 743506366


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        _sum = sum(nums)
        left_sum = 0
        for idx, num in enumerate(nums):
            if left_sum == _sum - left_sum - num:
                return idx
            left_sum += num
        return -1