# 1851 - Maximum Number of Events That Can Be Attended II
# Date: 2023-07-15
# Runtime: 934 ms, Memory: 158.5 MB
# Submission Id: 994733232


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        dp = [[-1] * n for _ in range(k+1)]
        
        def dfs(idx, count, prev_end):
            if idx == n or count == k:
                return 0
            if events[idx][0] <= prev_end:
                return dfs(idx + 1, count, prev_end)
            
            if dp[count][idx] != -1:
                return dp[count][idx]
            
            ans = max(dfs(idx+1, count, prev_end),
                      dfs(idx+1, count+1, events[idx][1]) + events[idx][2])
            dp[count][idx] = ans
            return ans
        
        return dfs(0, 0, -1)