# 2035 - Count Sub Islands
# Date: 2022-11-22
# Runtime: 8127 ms, Memory: 23.2 MB
# Submission Id: 847974741


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        len_r, len_c = len(grid1), len(grid1[0])
        for r in range(len_r):
            for c in range(len_c):
                if grid1[r][c] and grid2[r][c]:
                    grid2[r][c] = 2
        
        def dfs(row, col):
            stack = [(row, col)]
            is_valid = True
            while stack:
                r, c = stack.pop()
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    new_r, new_c = r+dx, c+dy
                    if 0 <= new_r < len_r and 0 <= new_c < len_c:
                        if grid2[new_r][new_c] == 1:
                            is_valid = False
                        if grid2[new_r][new_c] == 2:
                            grid2[new_r][new_c] = 0
                            stack.append((new_r, new_c)) 
            return is_valid
        
        count = 0
        for r in range(len_r):
            for c in range(len_c):
                if grid2[r][c] == 2:
                    grid2[r][c] = 0
                    count += dfs(r, c)
        return count