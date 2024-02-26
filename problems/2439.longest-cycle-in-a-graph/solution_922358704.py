# 2439 - Longest Cycle in a Graph
# Date: 2023-03-26
# Runtime: 1642 ms, Memory: 197.1 MB
# Submission Id: 922358704


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -1
        prev_seen = {}
        
        def dfs(node, length):
            if node == -1 or node in prev_seen:
                return -1
            if node in curr_seen:
                return length - curr_seen[node] + 1
            curr_seen[node] = length + 1
            return dfs(edges[node], length+1)
            
        for i in range(n):
            curr_seen = {}
            length = dfs(i, 0)
            ans = max(ans, length)
            prev_seen |= curr_seen
        return ans