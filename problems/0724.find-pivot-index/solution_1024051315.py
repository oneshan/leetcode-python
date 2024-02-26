# 0724 - Find Pivot Index
# Date: 2023-08-17
# Runtime: 138 ms, Memory: 17.7 MB
# Submission Id: 1024051315


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, sum(nums)
        for i in range(n):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1