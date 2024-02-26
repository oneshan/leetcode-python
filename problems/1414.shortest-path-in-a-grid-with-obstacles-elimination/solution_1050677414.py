# 1414 - Shortest Path in a Grid with Obstacles Elimination
# Date: 2023-09-16
# Runtime: 460 ms, Memory: 24.5 MB
# Submission Id: 1050677414


from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        len_r, len_c = len(grid), len(grid[0])
        
        seen = set((0, 0, k))
        queue = deque([(0, 0, k)])
        step = 0
        while queue:
            for _ in range(len(queue)):
                r, c, k = queue.popleft()
                if r == len_r -1 and c == len_c - 1:
                    return step
                for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= nr < len_r and 0 <= nc < len_c:
                        state = (nr, nc, k - grid[nr][nc])
                        if state not in seen and state[2] >= 0:
                            queue.append(state)
                            seen.add(state)
            step += 1
        return -1