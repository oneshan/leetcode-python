# 0813 - All Paths From Source to Target
# Date: 2023-09-19
# Runtime: 87 ms, Memory: 18.4 MB
# Submission Id: 1052753807


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        start, end = 0, len(graph)-1
        
        def backtrack(path, node):
            if node == end:
                ans.append(path[:])
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                backtrack(path, neighbor)
                path.pop()
                
        backtrack([0], start)
        return ans