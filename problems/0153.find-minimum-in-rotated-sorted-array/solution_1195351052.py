# 0153 - Find Minimum in Rotated Sorted Array
# Date: 2024-03-06
# Runtime: 39 ms, Memory: 16.8 MB
# Submission Id: 1195351052


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]