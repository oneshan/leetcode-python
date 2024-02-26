# 1738 - Maximal Network Rank
# Date: 2022-12-02
# Runtime: 535 ms, Memory: 16.2 MB
# Submission Id: 853465178


from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for i, j in roads:
            graph[i].add(j)
            graph[j].add(i)
            
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, len(graph[i]) + len(graph[j]) - (i in graph[j]))
        return ans