# 0200 - Number of Islands
# Date: 2024-04-19
# Runtime: 229 ms, Memory: 18.8 MB
# Submission Id: 1236315267


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        def traverse(row, col):
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
                    next_r, next_c = r+dr, c+dc
                    if 0 <= next_r < len_r and 0 <= next_c < len_c and grid[next_r][next_c] == '1':
                        grid[next_r][next_c] = 0
                        stack.append((next_r, next_c))

        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == '1':
                    ans += 1
                    traverse(r, c)
        return ans