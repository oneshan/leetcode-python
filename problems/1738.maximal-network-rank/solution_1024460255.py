# 1738 - Maximal Network Rank
# Date: 2023-08-18
# Runtime: 300 ms, Memory: 18.5 MB
# Submission Id: 1024460255


from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, len(graph[i]) + len(graph[j]) - (i in graph[j]))
        return ans