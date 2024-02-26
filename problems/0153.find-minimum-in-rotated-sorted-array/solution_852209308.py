# 0153 - Find Minimum in Rotated Sorted Array
# Date: 2022-11-30
# Runtime: 81 ms, Memory: 14.2 MB
# Submission Id: 852209308


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]