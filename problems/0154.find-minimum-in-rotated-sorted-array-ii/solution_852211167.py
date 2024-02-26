# 0154 - Find Minimum in Rotated Sorted Array II
# Date: 2022-11-30
# Runtime: 60 ms, Memory: 14.4 MB
# Submission Id: 852211167


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]