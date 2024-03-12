# 3313 - Maximum Strength of K Disjoint Subarrays
# Date: 2024-03-10
# Runtime: 2242 ms, Memory: 18.5 MB
# Submission Id: 1199284819


class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        prev = [0] * (n + 1)
        for i in range(k):
            dp = [float('-inf')] * (n + 1)
            mult = k-i if (k-i) & 1 else i-k
            max_sum = curr = float('-inf')
            for j in range(i+1, n+1):
                curr = max(curr, prev[j-1]) + nums[j-1] * mult
                max_sum = max(curr, max_sum)
                dp[j] = max(dp[j-1], max_sum)
            prev = dp

        return prev[-1]
