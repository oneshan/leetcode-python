# 0813 - All Paths From Source to Target
# Date: 2022-10-20
# Runtime: 109 ms, Memory: 15.6 MB
# Submission Id: 826423303


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        
        def dfs(node, path):
            if node == n-1:
                ans.append(path)
                return
            for neighbor in graph[node]:
                dfs(neighbor, path+[neighbor])
        
        dfs(0, [0])
        return ans