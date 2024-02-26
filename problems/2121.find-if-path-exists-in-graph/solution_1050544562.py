# 2121 - Find if Path Exists in Graph
# Date: 2023-09-16
# Runtime: 1829 ms, Memory: 316.1 MB
# Submission Id: 1050544562


from collections import defaultdict

class Solution:    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        # build graph - Time: O(E), Graph: O(V+E)
        graph = defaultdict(list)
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
        
        # DFS
        def dfs(node):
            if destination in seen:
                return
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        seen = {source}
        dfs(source)
        return destination in seen