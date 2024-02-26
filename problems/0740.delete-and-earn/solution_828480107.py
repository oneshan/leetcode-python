# 0740 - Delete and Earn
# Date: 2022-10-23
# Runtime: 652 ms, Memory: 16.2 MB
# Submission Id: 828480107


from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        point = defaultdict(int)
        for num in nums:
            point[num] += num
        
        dp = [0] * 10001
        dp[1] = point[1]
        
        for i in range(2, 10001):
            dp[i] = max(dp[i-1], dp[i-2] + point[i])
        return dp[-1]