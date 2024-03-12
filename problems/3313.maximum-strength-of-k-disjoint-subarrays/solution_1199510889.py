# 3313 - Maximum Strength of K Disjoint Subarrays
# Date: 2024-03-10
# Runtime: 1441 ms, Memory: 18.3 MB
# Submission Id: 1199510889


class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        prev = [0] * (n + 1)
        for i in range(k):
            dp = [float('-inf')] * (n + 1)
            mult = k-i if (k-i) & 1 else i-k
            left, curr = i, 0
            for right in range(i, n):
                if prev[right] > curr + prev[left]:
                    left, curr = right, 0
                curr += nums[right] * mult
                dp[right+1] = max(dp[right], curr + prev[left])
            prev = dp

        return prev[-1]
