# 0310 - Minimum Height Trees
# Date: 2023-09-29
# Runtime: 458 ms, Memory: 28.7 MB
# Submission Id: 1062084198


from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        graph = defaultdict(set)
        indegree = [0] * n
        
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            indegree[a] += 1
            indegree[b] += 1
        
        queue = deque([i for i in range(n) if indegree[i] == 1])
        while queue and n > 2:
            for _ in range(len(queue)):
                node = queue.popleft()
                n -= 1
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        queue.append(neighbor)
        return queue