# 0323 - Number of Connected Components in an Undirected Graph
# Date: 2022-10-20
# Runtime: 236 ms, Memory: 15.4 MB
# Submission Id: 826392899


from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        
        graph = defaultdict(list)
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
            
        ans = 0
        seen = set()
        for i in range(n):
            if i in seen:
                continue
            ans += 1
            stack = [i]
            seen.add(i)
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        stack.append(neighbor)
                        seen.add(neighbor)
        return ans