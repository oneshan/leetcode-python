# 0034 - Find First and Last Position of Element in Sorted Array
# Date: 2023-10-09
# Runtime: 79 ms, Memory: 17.6 MB
# Submission Id: 1070702975


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        n = len(nums)
        if not n:
            return ans
        
        left, right = 0, n-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1    
        ans[0] = left if nums[left] == target else -1
        
        right = n-1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1  
        ans[1] = left if nums[left] == target else -1

        return ans