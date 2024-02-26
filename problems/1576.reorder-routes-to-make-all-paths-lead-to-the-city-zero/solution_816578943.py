# 1576 - Reorder Routes to Make All Paths Lead to the City Zero
# Date: 2022-10-06
# Runtime: 2948 ms, Memory: 43.7 MB
# Submission Id: 816578943


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
        seen = set()
        ans = 0
        while stack:
            p = stack.pop()
            if p in seen:
                continue
            seen.add(p)
            for q in graph[p]:
                if q not in seen:
                    stack.append(q)
                    origin.discard((p, q))
        return len(connections) - len(origin)