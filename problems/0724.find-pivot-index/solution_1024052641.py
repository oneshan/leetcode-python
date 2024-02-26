# 0724 - Find Pivot Index
# Date: 2023-08-17
# Runtime: 113 ms, Memory: 17.5 MB
# Submission Id: 1024052641


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        curr, total = 0, sum(nums)
        for i in range(n):
            if curr == total - curr - nums[i]:
                return i
            curr += nums[i]
        return -1