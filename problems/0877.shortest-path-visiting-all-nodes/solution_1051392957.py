# 0877 - Shortest Path Visiting All Nodes
# Date: 2023-09-17
# Runtime: 159 ms, Memory: 21.3 MB
# Submission Id: 1051392957


from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        
        n = len(graph)
        end_mask = (1 << n) - 1
        
        queue = deque([(i, 1 << i) for i in range(n)])
        step = 0
        seen = set()
        while queue:
            for _ in range(len(queue)):
                node, mask = queue.popleft()
                if mask == end_mask:
                    return step
                for neighbor in graph[node]:
                    next_mask = mask | (1 << neighbor)
                    if (neighbor, next_mask) not in seen:
                        seen.add((neighbor, next_mask))
                        queue.append((neighbor, next_mask))
            step += 1