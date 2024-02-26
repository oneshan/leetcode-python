# 0033 - Search in Rotated Sorted Array
# Date: 2023-08-09
# Runtime: 51 ms, Memory: 16.7 MB
# Submission Id: 1015827248


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:  # nums[left:mid+1] sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:                       # nums[mid:right+1] sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1