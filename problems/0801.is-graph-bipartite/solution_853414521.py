# 0801 - Is Graph Bipartite?
# Date: 2022-12-02
# Runtime: 492 ms, Memory: 14.4 MB
# Submission Id: 853414521


from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        def dfs(start):
            queue = deque([start])
            color[start] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 ^ color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
            return True
        
        for node in range(len(graph)):
            if node not in color:
                if not dfs(node):
                    return False
        return True