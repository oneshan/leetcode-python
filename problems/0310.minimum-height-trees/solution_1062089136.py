# 0310 - Minimum Height Trees
# Date: 2023-09-29
# Runtime: 450 ms, Memory: 28.5 MB
# Submission Id: 1062089136


from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        queue = deque([i for i in range(n) if len(graph[i]) == 1])
        while queue and n > 2:
            for _ in range(len(queue)):
                node = queue.popleft()
                n -= 1
                neighbor = graph[node].pop()
                graph[neighbor].discard(node)
                if len(graph[neighbor]) == 1:
                    queue.append(neighbor)
        return queue