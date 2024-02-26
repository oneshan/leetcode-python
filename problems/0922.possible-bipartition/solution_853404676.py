# 0922 - Possible Bipartition
# Date: 2022-12-02
# Runtime: 997 ms, Memory: 20.1 MB
# Submission Id: 853404676


from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        RED, BLUE = 0, 1
        
        def bfs(start):
            queue = deque([start])
            color[start] = RED
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == color[node]:
                        return False
                    if color[neighbor] == -1:
                        color[neighbor] = BLUE if color[node] == RED else RED
                        queue.append(neighbor)
            return True
        
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
               
        color = [-1] * (n+1)
        for i in range(1, n+1):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True