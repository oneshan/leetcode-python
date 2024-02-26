# 2582 - Minimum Score of a Path Between Two Cities
# Date: 2023-03-22
# Runtime: 1667 ms, Memory: 67.8 MB
# Submission Id: 919826774


from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, w in roads:
            graph[a].append((b, w))
            graph[b].append((a, w))
        
        ans = float('inf')
        queue = deque([1])
        seen = {1}
        while queue:
            node = queue.popleft()
            for neighbor, weight in graph[node]:
                ans = min(ans, weight)
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        
        return ans