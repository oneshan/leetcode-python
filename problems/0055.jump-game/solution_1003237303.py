# 0055 - Jump Game
# Date: 2023-07-25
# Runtime: 7569 ms, Memory: 57.3 MB
# Submission Id: 1003237303


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @cache
        def dp(i):
            if i == n - 1:
                return True
            for j in range(i+1, min(n, i+nums[i]+1)):
                if dp(j):
                    return True
            return False
        
        return dp(0)