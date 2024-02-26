# 0813 - All Paths From Source to Target
# Date: 2022-10-20
# Runtime: 180 ms, Memory: 16 MB
# Submission Id: 826453366


from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        
        queue = deque([[0, [0]]])
        while queue:
            node, path = queue.popleft()
            if node == n-1:
                ans.append(path)
                continue
            for neighbor in graph[node]:
                queue.append([neighbor, path+[neighbor]])
        
        return ans