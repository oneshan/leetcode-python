# 1102 - Check If a Number Is Majority Element in a Sorted Array
# Date: 2023-07-22
# Runtime: 49 ms, Memory: 16.3 MB
# Submission Id: 1000682711


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left, right, idx = 0, n-1, n
        
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] >= target:
                right = mid - 1
                idx = mid
            else:
                left = mid + 1
        return idx + (n >> 1) < n and nums[idx+(n>>1)] == target