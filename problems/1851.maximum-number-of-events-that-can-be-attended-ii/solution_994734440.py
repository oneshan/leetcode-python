# 1851 - Maximum Number of Events That Can Be Attended II
# Date: 2023-07-15
# Runtime: 1254 ms, Memory: 202.8 MB
# Submission Id: 994734440


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        
        @cache
        def dfs(idx, count, prev_end):
            if idx == n or count == k:
                return 0
            if events[idx][0] <= prev_end:
                return dfs(idx + 1, count, prev_end)            
            return max(
                dfs(idx+1, count, prev_end),
                dfs(idx+1, count+1, events[idx][1]) + events[idx][2]
            )
        
        return dfs(0, 0, -1)