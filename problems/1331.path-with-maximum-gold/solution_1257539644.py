# 1331 - Path with Maximum Gold
# Date: 2024-05-14
# Runtime: 6423 ms, Memory: 49.8 MB
# Submission Id: 1257539644


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])

        def bfs(r, c):
            res = 0
            queue = deque([(r, c, grid[r][c], {(r, c)})])
            while queue:
                r, c, gold, seen = queue.popleft()
                res = max(res, gold)
                for nr, nc in (r+1, c), (r, c+1), (r-1, c), (r, c-1):
                    if 0 <= nr < len_r and 0 <= nc < len_c and grid[nr][nc] and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        queue.append((nr, nc, gold + grid[nr][nc], seen.copy()))
                        seen.remove((nr, nc))
            return res

        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c]:
                    ans = max(ans, bfs(r, c))
        return ans