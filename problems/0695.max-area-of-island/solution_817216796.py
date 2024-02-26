# 0695 - Max Area of Island
# Date: 2022-10-07
# Runtime: 370 ms, Memory: 14.3 MB
# Submission Id: 817216796


from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        seen = set()
        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == 0 or (r, c) in seen:
                    continue
                shape = 0
                queue = deque([(r, c)])
                seen.add((r, c))
                while queue:
                    x, y = queue.popleft()
                    shape += 1
                    for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                        new_x, new_y = x+dx, y+dy
                        if (0 <= new_x < len_r and 0 <= new_y < len_c
                            and grid[new_x][new_y]
                            and (new_x, new_y) not in seen):
                            queue.append((new_x, new_y))
                            seen.add((new_x, new_y))
                ans = max(ans, shape)

        return ans