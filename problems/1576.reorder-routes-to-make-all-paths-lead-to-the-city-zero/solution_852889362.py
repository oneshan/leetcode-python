# 1576 - Reorder Routes to Make All Paths Lead to the City Zero
# Date: 2022-12-01
# Runtime: 2999 ms, Memory: 42.6 MB
# Submission Id: 852889362


from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        origin = set()
        graph = defaultdict(list)
        for p, q in connections:
            origin.add((p, q))
            graph[p].append(q)
            graph[q].append(p)
        
        stack = [0]
        seen = {0}
        ans = 0
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in origin:
                        ans += 1
                    seen.add(neighbor)
                    stack.append(neighbor)
                    
        return ans