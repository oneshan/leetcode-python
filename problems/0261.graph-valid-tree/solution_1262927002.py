# 0261 - Graph Valid Tree
# Date: 2024-05-20
# Runtime: 78 ms, Memory: 18.4 MB
# Submission Id: 1262927002




class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        stack = [(0, -1)]
        seen = {0}
        while stack:
            node, parent = stack.pop()
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in seen:
                    return False
                seen.add(neighbor)
                stack.append((neighbor, node))
        return len(seen) == n