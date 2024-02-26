# 2450 - Minimum Replacements to Sort the Array
# Date: 2023-08-30
# Runtime: 504 ms, Memory: 27.7 MB
# Submission Id: 1035667405


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0
        for i in range(n-1, 0, -1):
            if nums[i] >= nums[i-1]:
                continue
                
            count = (nums[i] + nums[i-1] - 1) // nums[i]
            nums[i-1] = nums[i-1] // count
            ans += count - 1
        return ans