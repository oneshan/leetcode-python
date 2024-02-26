# 2445 - Reachable Nodes With Restrictions
# Date: 2023-09-16
# Runtime: 1352 ms, Memory: 74.6 MB
# Submission Id: 1050553456


from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
           
        ans = 0
        stack = [0]
        seen = set(restricted)
        seen.add(0)
        
        while stack:
            node = stack.pop()
            ans += 1
            for neighbor in graph[node]:
                if neighbor not in seen:
                    stack.append(neighbor)
                    seen.add(neighbor)
        return ans