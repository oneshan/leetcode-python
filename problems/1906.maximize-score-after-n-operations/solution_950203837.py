# 1906 - Maximize Score After N Operations
# Date: 2023-05-14
# Runtime: 2591 ms, Memory: 25.9 MB
# Submission Id: 950203837


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        @cache
        def dp(mask, k):
            if mask == 0:
                return 0
            ans = 0
            for i in range(n):
                if not mask & (1 << i): continue
                for j in range(i+1, n):
                    if not mask & (1 << j): continue
                    new_mask = mask ^ (1 << i) ^ (1 << j)
                    ans = max(ans, k * gcd(nums[i], nums[j]) + dp(new_mask, k+1))
            return ans

        return dp((1 << n) - 1, 1)