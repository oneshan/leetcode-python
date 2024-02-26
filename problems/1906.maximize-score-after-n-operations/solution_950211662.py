# 1906 - Maximize Score After N Operations
# Date: 2023-05-14
# Runtime: 2393 ms, Memory: 16.6 MB
# Submission Id: 950211662


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        end_mask = (1 << n) - 1
        
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        dp = [0] * (1 << n)
        for mask in range(end_mask, -1, -1):
            if mask.bit_count() & 1:
                continue
            k = (mask.bit_count() >> 1) + 1
            for i in range(n):
                if mask & (1 << i): continue
                for j in range(i+1, n):
                    if mask & (1 << j): continue
                    dp[mask] = max(dp[mask], k * gcd(nums[i], nums[j]) + dp[mask | (1<<i) | (1<<j)])
        return dp[0]