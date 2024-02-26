# 0035 - Search Insert Position
# Date: 2022-11-20
# Runtime: 57 ms, Memory: 14.7 MB
# Submission Id: 846878228


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left