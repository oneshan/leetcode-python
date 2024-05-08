# 3158 - Maximum Length of Semi-Decreasing Subarrays
# Date: 2024-05-07
# Runtime: 452 ms, Memory: 31.6 MB
# Submission Id: 1251575482


class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        right_min = [nums[-1]] * n
        for i in range(n-2, -1, -1):
            right_min[i] = min(right_min[i+1], nums[i])
        
        ans = 0
        left = right = 0            
        for left in range(n):
            while right < n and right_min[right] < nums[left]:
                right += 1
            ans = max(ans, right-left)
            if right == n:
                break
        return ans