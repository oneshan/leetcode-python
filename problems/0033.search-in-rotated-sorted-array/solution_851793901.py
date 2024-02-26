# 0033 - Search in Rotated Sorted Array
# Date: 2022-11-29
# Runtime: 63 ms, Memory: 14.2 MB
# Submission Id: 851793901


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
                    right = mid
                else:
                    left = mid + 1
            else:                       # nums[mid:right+1] sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return -1