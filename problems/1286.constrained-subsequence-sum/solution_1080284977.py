# 1286 - Constrained Subsequence Sum
# Date: 2023-10-21
# Runtime: 1273 ms, Memory: 29.9 MB
# Submission Id: 1080284977


from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        queue = deque()
        
        for i in range(n):
            if queue and i - queue[0] > k:
                queue.popleft()
            
            dp[i] = (dp[queue[0]] if queue else 0) + nums[i]
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()
            
            if dp[i] > 0:
                queue.append(i)
        
        return max(dp)