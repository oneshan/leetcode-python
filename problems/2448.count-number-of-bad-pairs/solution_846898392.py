# 2448 - Count Number of Bad Pairs
# Date: 2022-11-20
# Runtime: 2044 ms, Memory: 33.6 MB
# Submission Id: 846898392


from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n-1) // 2
        good = 0
        
        dp = defaultdict(int)
        for idx, num in enumerate(nums):
            target = idx - num
            good += dp[target]
            dp[target] += 1
        return total - good