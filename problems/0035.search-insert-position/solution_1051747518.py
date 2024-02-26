# 0035 - Search Insert Position
# Date: 2023-09-17
# Runtime: 57 ms, Memory: 17.2 MB
# Submission Id: 1051747518


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