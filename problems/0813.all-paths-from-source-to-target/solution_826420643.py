# 0813 - All Paths From Source to Target
# Date: 2022-10-20
# Runtime: 252 ms, Memory: 15.7 MB
# Submission Id: 826420643


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        
        def dfs(curr, path):
            if curr == n-1:
                ans.append(path[:])
                return
            for neighbor in graph[curr]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
        
        dfs(0, [0])
        return ans