# 0695 - Max Area of Island
# Date: 2022-10-07
# Runtime: 295 ms, Memory: 14.7 MB
# Submission Id: 817213000


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        seen = set()
        
        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] and (r, c) not in seen:
                    shape = 0
                    stack = [(r, c)]
                    while stack:
                        x, y = stack.pop()
                        if grid[x][y] == 0 or (x,y) in seen:
                            continue
                        shape += 1
                        seen.add((x, y))
                        if x > 0: stack.append((x-1, y))
                        if y > 0: stack.append((x, y-1))
                        if x < len_r-1: stack.append((x+1, y))
                        if y < len_c-1: stack.append((x, y+1))
                    ans = max(ans, shape)

        return ans