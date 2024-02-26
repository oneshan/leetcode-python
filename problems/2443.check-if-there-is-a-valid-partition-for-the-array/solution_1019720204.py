# 2443 - Check if There is a Valid Partition For The Array
# Date: 2023-08-13
# Runtime: 974 ms, Memory: 30.5 MB
# Submission Id: 1019720204


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        dp = [False] * (n+1)
        dp[0] = True
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                dp[i+1] |= dp[i-1]
            if i > 1 and nums[i] == nums[i-1] == nums[i-2]:
                dp[i+1] |= dp[i-2]
            if i > 1 and nums[i] == nums[i-1] + 1 == nums[i-2] + 2:
                dp[i+1] |= dp[i-2]
                
        return dp[-1]