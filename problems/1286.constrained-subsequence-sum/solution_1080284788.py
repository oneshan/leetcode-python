# 1286 - Constrained Subsequence Sum
# Date: 2023-10-21
# Runtime: 1275 ms, Memory: 29.9 MB
# Submission Id: 1080284788


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = deque()
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            if queue and i - queue[0] > k:
                queue.popleft()
            
            dp[i] = (dp[queue[0]] if queue else 0) + nums[i]
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()
            
            if dp[i] > 0:
                queue.append(i)
                
        return max(dp)