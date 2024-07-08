# 0081 - Search in Rotated Sorted Array II
# Date: 2024-05-13
# Runtime: 55 ms, Memory: 17.2 MB
# Submission Id: 1256730626


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid]:
                left += 1
                continue
            if nums[right] == nums[mid]:
                right -= 1
                continue
            
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False