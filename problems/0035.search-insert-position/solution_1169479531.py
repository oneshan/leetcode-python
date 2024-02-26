# 0035 - Search Insert Position
# Date: 2024-02-08
# Runtime: 47 ms, Memory: 17.3 MB
# Submission Id: 1169479531


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left