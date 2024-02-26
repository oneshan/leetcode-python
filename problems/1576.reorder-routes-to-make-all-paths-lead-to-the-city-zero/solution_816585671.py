# 1576 - Reorder Routes to Make All Paths Lead to the City Zero
# Date: 2022-10-06
# Runtime: 3158 ms, Memory: 47.7 MB
# Submission Id: 816585671


from collections import defaultdict, deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        for p, q in connections:
            graph[p].add((q, True))
            graph[q].add((p, False))
        
        queue = deque([(0, False)])
        seen = set()
        ans = 0
        while queue:
            p, need_changed = queue.popleft()
            seen.add(p)
            if need_changed:
                ans += 1
            for q_pair in graph[p]:
                if q_pair[0] not in seen:
                    queue.append(q_pair)
        return ans