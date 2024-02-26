# 1576 - Reorder Routes to Make All Paths Lead to the City Zero
# Date: 2022-10-06
# Runtime: 2852 ms, Memory: 43.1 MB
# Submission Id: 816590247


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
                    if (p, q) in origin:
                        ans += 1
        return ans