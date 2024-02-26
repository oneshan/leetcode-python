# 2121 - Find if Path Exists in Graph
# Date: 2022-10-20
# Runtime: 2906 ms, Memory: 106.3 MB
# Submission Id: 826410402


from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph = defaultdict(list)
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
            
        stack = [source]
        seen = set([source])
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor == destination:
                    return True
                if neighbor in seen:
                    continue
                stack.append(neighbor)
                seen.add(neighbor)
        return False