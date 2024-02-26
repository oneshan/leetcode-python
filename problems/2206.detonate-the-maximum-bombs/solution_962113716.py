# 2206 - Detonate the Maximum Bombs
# Date: 2023-06-02
# Runtime: 642 ms, Memory: 16.5 MB
# Submission Id: 962113716


from collections import defaultdict, deque

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        
        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(i+1, n):
                xj, yj, rj = bombs[j]
                dist = (xi - xj) ** 2 + (yi - yj) ** 2
                if ri ** 2 >= dist:
                    graph[i].append(j)
                if rj ** 2 >= dist:
                    graph[j].append(i)
        
        
        def bfs(i):
            queue = deque([i])
            seen = {i}
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            return len(seen)
        
        
        ans = 0
        for i in range(n):
            ans = max(ans, bfs(i))
            
        return ans