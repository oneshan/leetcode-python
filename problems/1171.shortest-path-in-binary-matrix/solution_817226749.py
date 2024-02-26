# 1171 - Shortest Path in Binary Matrix
# Date: 2022-10-07
# Runtime: 1652 ms, Memory: 15.4 MB
# Submission Id: 817226749


from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1
        
        def valid(x, y):
            return 0 <= x < len_r and 0 <= y < len_c and grid[x][y] == 0
            
        seen = set((0, 0))
        queue = deque([(0, 0, 1)])
        while queue:
            x, y, steps = queue.popleft()
            if x == len_r -1 and y == len_c -1:
                return steps
            dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            for dx, dy in dirs:
                next_x, next_y = x+dx, y+dy
                if valid(next_x, next_y) and (next_x, next_y) not in seen:
                    seen.add((next_x, next_y))
                    queue.append((next_x, next_y, steps+1))
        return -1