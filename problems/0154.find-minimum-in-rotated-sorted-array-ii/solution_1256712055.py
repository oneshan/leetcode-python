# 0154 - Find Minimum in Rotated Sorted Array II
# Date: 2024-05-13
# Runtime: 45 ms, Memory: 17 MB
# Submission Id: 1256712055


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # search right
                left = mid + 1
            elif nums[mid] < nums[right]:
                # search left
                right = mid
            else:
                right -= 1

        return nums[left]