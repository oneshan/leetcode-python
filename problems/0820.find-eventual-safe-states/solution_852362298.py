# 0820 - Find Eventual Safe States
# Date: 2022-11-30
# Runtime: 829 ms, Memory: 25 MB
# Submission Id: 852362298


from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        
        graph = list(map(set, graph))
        reverse_graph = [set() for _ in range(n)]
        queue = deque()
        for i, js in enumerate(graph):
            if not js:
                queue.append(i)
            for j in js:
                reverse_graph[j].add(i)
        
        while queue:
            j = queue.popleft()
            safe[j] = True
            for i in reverse_graph[j]:
                graph[i].remove(j)
                if len(graph[i]) == 0:
                    queue.append(i)
        return [i for i in range(n) if safe[i]]