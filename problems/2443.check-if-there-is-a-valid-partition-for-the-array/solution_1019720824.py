# 2443 - Check if There is a Valid Partition For The Array
# Date: 2023-08-13
# Runtime: 925 ms, Memory: 32.2 MB
# Submission Id: 1019720824


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        dp = [True, False, False]
        
        for i in range(n):
            ans = False
            if i > 0 and nums[i] == nums[i-1]:
                ans |= dp[(i-1) % 3]
            if i > 1 and nums[i] == nums[i-1] == nums[i-2]:
                ans |= dp[(i-2) % 3]
            if i > 1 and nums[i] == nums[i-1] + 1 == nums[i-2] + 2:
                ans |= dp[(i-2) % 3]
            dp[(i+1) % 3] = ans
                
        return dp[n % 3]