# 0153 - Find Minimum in Rotated Sorted Array
# Date: 2022-10-20
# Runtime: 106 ms, Memory: 14.3 MB
# Submission Id: 826596549


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1                
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[right]