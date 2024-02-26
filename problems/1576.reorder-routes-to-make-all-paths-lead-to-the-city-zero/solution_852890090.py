# 1576 - Reorder Routes to Make All Paths Lead to the City Zero
# Date: 2022-12-01
# Runtime: 2637 ms, Memory: 43.4 MB
# Submission Id: 852890090


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
            p = stack.pop()
            for q in graph[p]:
                if q not in seen:
                    seen.add(q)
                    stack.append(q)
                    origin.discard((p, q))
        return len(connections) - len(origin)