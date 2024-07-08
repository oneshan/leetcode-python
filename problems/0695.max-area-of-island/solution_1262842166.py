# 0695 - Max Area of Island
# Date: 2024-05-20
# Runtime: 107 ms, Memory: 16.7 MB
# Submission Id: 1262842166


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])

        def traverse(r, c):
            grid[r][c] = area = 0
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                area += 1
                for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= nr < len_r and 0 <= nc < len_c and grid[nr][nc]:
                        grid[nr][nc] = 0
                        stack.append((nr, nc))

            return area

        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c]:
                    ans = max(ans, traverse(r, c))
        return ans