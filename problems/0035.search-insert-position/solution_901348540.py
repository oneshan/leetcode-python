# 0035 - Search Insert Position
# Date: 2023-02-20
# Runtime: 42 ms, Memory: 14.7 MB
# Submission Id: 901348540


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left