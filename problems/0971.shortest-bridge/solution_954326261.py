# 0971 - Shortest Bridge
# Date: 2023-05-21
# Runtime: 393 ms, Memory: 19.2 MB
# Submission Id: 954326261


from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        
        def dfs(r, c):
            grid[r][c] = 2
            queue.append((r, c))
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                next_r, next_c = dx+r, dy+c
                if 0 <= next_r < n and 0 <= next_c < n:
                    if grid[next_r][next_c] == 1:
                        dfs(next_r, next_c)
        
        def bfs():
            distance = 0
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        next_r, next_c = dx+r, dy+c
                        if 0 <= next_r < n and 0 <= next_c < n:
                            if grid[next_r][next_c] == 1:
                                return distance
                            if grid[next_r][next_c] == 0:
                                queue.append((next_r, next_c))
                                grid[next_r][next_c] = 2
                distance += 1
        
        first_found = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    first_found = True
                    break
            if first_found:
                break
                
        return bfs()
        