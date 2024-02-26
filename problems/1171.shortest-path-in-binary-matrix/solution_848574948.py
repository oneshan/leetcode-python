# 1171 - Shortest Path in Binary Matrix
# Date: 2022-11-23
# Runtime: 578 ms, Memory: 14.1 MB
# Submission Id: 848574948


from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        if len_r == len_c == 1:
            return 1
        
        grid[0][0] = 1
        queue = deque([(0, 0, 1)])
        while queue:
            x, y, steps = queue.popleft()
            dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            for dx, dy in dirs:
                next_x, next_y = x+dx, y+dy
                if next_x == len_r -1 and next_y == len_c -1:
                    return steps+1
                if 0 <= next_x < len_r and 0 <= next_y < len_c and grid[next_x][next_y] == 0:
                    queue.append((next_x, next_y, steps+1))
                    grid[next_x][next_y] = 1
        return -1