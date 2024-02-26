# 2218 - Paths in Maze That Lead to Same Room
# Date: 2023-09-16
# Runtime: 615 ms, Memory: 35.3 MB
# Submission Id: 1050547998


from collections import defaultdict

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        ans = 0
        for p, q in corridors:
            graph[p].add(q)
            graph[q].add(p)
            ans += len(graph[p] & (graph[q]))
        return ans