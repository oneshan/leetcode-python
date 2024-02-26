# 0033 - Search in Rotated Sorted Array
# Date: 2022-05-28
# Runtime: 77 ms, Memory: 14.2 MB
# Submission Id: 708937226


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if pivot < right and nums[pivot] > nums[pivot + 1]:
                break
            if nums[pivot] < nums[left]:
                right = pivot - 1
            else:
                left = pivot + 1
                
        if nums[0] > target:
            left, right = pivot + 1, len(nums) - 1
        else:
            left, right = 0, pivot
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1