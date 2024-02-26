# 0035 - Search Insert Position
# Date: 2022-05-09
# Runtime: 63 ms, Memory: 14.7 MB
# Submission Id: 696174014


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left