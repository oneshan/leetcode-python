# 0034 - Find First and Last Position of Element in Sorted Array
# Date: 2022-11-24
# Runtime: 91 ms, Memory: 15.5 MB
# Submission Id: 849109583


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        n = len(nums)
        
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans[0] = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans[1] = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return ans