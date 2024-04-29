# 2103 - Find All Groups of Farmland
# Date: 2024-04-20
# Runtime: 915 ms, Memory: 29.8 MB
# Submission Id: 1237133939


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(land), len(land[0])
        ans = []

        def dfs(r, c):
            min_r = max_r = r
            min_c = max_c = c
            land[r][c] = 0
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                for nr, nc in (r-1, c), (r, c-1), (r+1, c), (r, c+1):
                    if 0 <= nr < len_r and 0 <= nc < len_c and land[nr][nc]:
                        stack.append((nr, nc))
                        min_r = min(min_r, nr)
                        max_r = max(max_r, nr)
                        min_c = min(min_c, nc)
                        max_c = max(max_c, nc)
                        land[nr][nc] = 0
            ans.append([min_r, min_c, max_r, max_c])

        for r in range(len_r):
            for c in range(len_c):
                if land[r][c] == 1:
                    dfs(r ,c)

        return ans