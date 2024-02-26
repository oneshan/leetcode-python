# 0922 - Possible Bipartition
# Date: 2022-12-02
# Runtime: 1846 ms, Memory: 20.2 MB
# Submission Id: 853405780


from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        RED, BLUE = 0, 1
        
        def dfs(start):
            stack = [start]
            color[start] = RED
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if color[neighbor] == color[node]:
                        return False
                    if color[neighbor] == -1:
                        color[neighbor] = BLUE if color[node] == RED else RED
                        stack.append(neighbor)
            return True
        
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
               
        color = [-1] * (n+1)
        for i in range(1, n+1):
            if color[i] == -1:
                if not dfs(i):
                    return False
        return True