# 0820 - Find Eventual Safe States
# Date: 2023-07-12
# Runtime: 651 ms, Memory: 23.9 MB
# Submission Id: 992418411


from collections import defaultdict

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)
        n = len(graph)

        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK
            
            color[node] = GRAY
            for neighbor in graph[node]:
                if color[neighbor] == BLACK:
                    continue
                if color[neighbor] == GRAY or not dfs(neighbor):
                    return False
                
            color[node] = BLACK
            return True
        
        return [i for i in range(n) if dfs(i)]