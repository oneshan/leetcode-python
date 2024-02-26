# 0200 - Number of Islands
# Date: 2022-11-19
# Runtime: 669 ms, Memory: 16.2 MB
# Submission Id: 846220162


from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        len_r, len_c = len(grid), len(grid[0])
        ans = 0
        
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == '0':
                    continue
                ans += 1
                queue = deque([(r,c)])
                while queue:
                    next_r, next_c = queue.popleft()
                    if grid[next_r][next_c] == '1':
                        if next_r > 0: queue.append((next_r-1, next_c))
                        if next_r < len_r - 1: queue.append((next_r+1, next_c))
                        if next_c > 0: queue.append((next_r, next_c-1))
                        if next_c < len_c -1: queue.append((next_r, next_c+1))
                    grid[next_r][next_c] = '0'
        return ans