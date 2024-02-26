# 0922 - Possible Bipartition
# Date: 2022-12-02
# Runtime: 725 ms, Memory: 21.9 MB
# Submission Id: 853406347


from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        RED, BLUE = 0, 1
        
        def dfs(node, node_color):
            color[node] = node_color
            for neighbor in graph[node]:
                if color[neighbor] == color[node]:
                    return False
                if color[neighbor] == -1:
                    if not dfs(neighbor, BLUE if color[node] == RED else RED):
                        return False
            return True
        
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
               
        color = [-1] * (n+1)
        for i in range(1, n+1):
            if color[i] == -1:
                if not dfs(i, RED):
                    return False
        return True