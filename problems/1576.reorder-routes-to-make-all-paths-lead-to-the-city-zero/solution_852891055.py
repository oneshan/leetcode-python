# 1576 - Reorder Routes to Make All Paths Lead to the City Zero
# Date: 2022-12-01
# Runtime: 2251 ms, Memory: 47.8 MB
# Submission Id: 852891055


from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        for p, q in connections:
            graph[p].add((q, True))
            graph[q].add((p, False))
        
        stack = [(0, False)]
        seen = {0}
        ans = 0
        while stack:
            p, need_changed = stack.pop()
            seen.add(p)
            if need_changed:
                ans += 1
            for q_pair in graph[p]:
                if q_pair[0] not in seen:
                    stack.append(q_pair)
        return ans