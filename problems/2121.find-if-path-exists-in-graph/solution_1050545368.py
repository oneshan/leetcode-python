# 2121 - Find if Path Exists in Graph
# Date: 2023-09-16
# Runtime: 1894 ms, Memory: 313.4 MB
# Submission Id: 1050545368


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
            if node == destination:
                return True
            if node not in seen:
                seen.add(node)
                for neighbor in graph[node]:
                    if dfs(neighbor):
                        return True
            return False
        
        seen = set()
        return dfs(source)