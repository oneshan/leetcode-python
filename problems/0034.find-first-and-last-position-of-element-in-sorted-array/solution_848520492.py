# 0034 - Find First and Last Position of Element in Sorted Array
# Date: 2022-11-23
# Runtime: 223 ms, Memory: 15.5 MB
# Submission Id: 848520492


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        n = len(nums)
        
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        ans[0] = left if 0 <= left < n and nums[left] == target else -1
                
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        left -= 1
        ans[1] = left if 0 <= left < n and nums[left] == target else -1
        
        return ans