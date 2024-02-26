# 0323 - Number of Connected Components in an Undirected Graph
# Date: 2023-09-16
# Runtime: 107 ms, Memory: 17.9 MB
# Submission Id: 1050549913


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
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
            while stack:
                node = stack.pop()
                seen.add(node)
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
        return ans