# 2582 - Minimum Score of a Path Between Two Cities
# Date: 2023-03-22
# Runtime: 1722 ms, Memory: 69 MB
# Submission Id: 919827786


from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, w in roads:
            graph[a].append((b, w))
            graph[b].append((a, w))
        
        ans = float('inf')
        stack = [1]
        seen = {1}
        while stack:
            node = stack.pop()
            for neighbor, weight in graph[node]:
                ans = min(ans, weight)
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        
        return ans