# 2121 - Find if Path Exists in Graph
# Date: 2022-10-07
# Runtime: 4310 ms, Memory: 105.2 MB
# Submission Id: 817198293


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
        stack = [source]
        seen = {source}
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor == destination:
                    return True
                if neighbor not in seen:
                    stack.append(neighbor)
                    seen.add(neighbor)
        return False