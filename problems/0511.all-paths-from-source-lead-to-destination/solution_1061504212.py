# 0511 - All Paths from Source Lead to Destination
# Date: 2023-09-28
# Runtime: 284 ms, Memory: 22.6 MB
# Submission Id: 1061504212


from collections import defaultdict

class Solution:
    GRAY = 1
    BLACK = 2
    
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        color = [None] * n
        
        def dfs(node):
            if not graph[node]:
                return node == destination
            if color[node]:
                return color[node] == Solution.BLACK

            color[node] = Solution.GRAY
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            color[node] = Solution.BLACK
            return True
        
        return dfs(source)