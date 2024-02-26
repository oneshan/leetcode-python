# 1906 - Maximize Score After N Operations
# Date: 2023-05-14
# Runtime: 2587 ms, Memory: 25.5 MB
# Submission Id: 950204352


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        final = (1 << n) - 1
        
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        @cache
        def dp(mask, k):
            if mask == final:
                return 0
            ans = 0
            for i in range(n):
                if mask & (1 << i): continue
                for j in range(i+1, n):
                    if mask & (1 << j): continue
                    new_mask = mask | (1 << i) | (1 << j)
                    ans = max(ans, k * gcd(nums[i], nums[j]) + dp(new_mask, k+1))
            return ans

        return dp(0, 1)