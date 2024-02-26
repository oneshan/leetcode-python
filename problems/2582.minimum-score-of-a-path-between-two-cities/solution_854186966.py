# 2582 - Minimum Score of a Path Between Two Cities
# Date: 2022-12-04
# Runtime: 3453 ms, Memory: 91.6 MB
# Submission Id: 854186966


from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, w in roads:
            graph[a].append((b, w))
            graph[b].append((a, w))
        
        ans = float('inf')
        stack =[1]
        seen = {(1, 1)}
        while stack:
            node = stack.pop()
            for neighbor, weight in graph[node]:
                if (node, neighbor) not in seen:
                    ans = min(ans, weight)
                    seen.add((node, neighbor))
                    seen.add((neighbor, node))
                    stack.append(neighbor)
        
        return ans