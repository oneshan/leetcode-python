# 0081 - Search in Rotated Sorted Array II
# Date: 2023-08-10
# Runtime: 55 ms, Memory: 17 MB
# Submission Id: 1017056002


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            while left < right and nums[left] == nums[left+1]:
                left += 1
            if nums[left] == target:
                return True
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            if nums[right] == target:
                return True
            
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] <= nums[mid]:
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False