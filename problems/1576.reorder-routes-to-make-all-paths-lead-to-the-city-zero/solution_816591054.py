# 1576 - Reorder Routes to Make All Paths Lead to the City Zero
# Date: 2022-10-07
# Runtime: 2958 ms, Memory: 73.3 MB
# Submission Id: 816591054


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
        def dfs(node):
            ans = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in origin:
                        ans += 1
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans
                    
        return dfs(0)