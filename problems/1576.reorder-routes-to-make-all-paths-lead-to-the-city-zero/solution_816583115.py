# 1576 - Reorder Routes to Make All Paths Lead to the City Zero
# Date: 2022-10-06
# Runtime: 2653 ms, Memory: 47.5 MB
# Submission Id: 816583115


from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        for p, q in connections:
            graph[p].add((q, True))
            graph[q].add((p, False))
        
        stack = [(0, False)]
        seen = set()
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