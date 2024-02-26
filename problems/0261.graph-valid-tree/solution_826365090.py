# 0261 - Graph Valid Tree
# Date: 2022-10-20
# Runtime: 221 ms, Memory: 15.6 MB
# Submission Id: 826365090


from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
            
        seen = set()
        stack = [0]
        while stack:
            node = stack.pop()
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor in seen:
                    continue
                stack.append(neighbor)
        return len(seen) == n