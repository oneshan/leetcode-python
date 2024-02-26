# 1171 - Shortest Path in Binary Matrix
# Date: 2023-09-16
# Runtime: 528 ms, Memory: 16.5 MB
# Submission Id: 1050644217


from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        if len_r == len_c == 1:
            return 1

        def valid(row, col):
            return 0 <= row < len_r and 0 <= col < len_c and grid[row][col] == 0
        
        grid[0][0] = 1
        queue = deque([(0, 0)])
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
                for dx, dy in dirs:
                    next_x, next_y = x+dx, y+dy
                    if next_x == len_r -1 and next_y == len_c -1:
                        return step + 1
                    if valid(next_x, next_y):
                        queue.append((next_x, next_y))
                        grid[next_x][next_y] = 1
        return -1