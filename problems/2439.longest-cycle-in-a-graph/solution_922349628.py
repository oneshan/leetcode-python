# 2439 - Longest Cycle in a Graph
# Date: 2023-03-26
# Runtime: 1255 ms, Memory: 186.7 MB
# Submission Id: 922349628


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        seen = set()
        ans = -1
        
        def dfs(node, dist):
            nonlocal ans
            seen.add(node)
            neighbor = edges[node]
            if neighbor != -1 and neighbor not in seen:
                dist[neighbor] = dist[node] + 1
                dfs(neighbor, dist)
            else:
                if neighbor in dist:
                    ans = max(ans, dist[node] - dist[neighbor] + 1)
            
        for node in range(n):
            if node in seen:
                continue
            dfs(node, {node: 1})
        return ans
