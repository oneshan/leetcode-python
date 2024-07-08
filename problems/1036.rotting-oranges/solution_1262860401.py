# 1036 - Rotting Oranges
# Date: 2024-05-20
# Runtime: 50 ms, Memory: 16.6 MB
# Submission Id: 1262860401


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        
        rotten = []
        fresh = 0
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        queue = deque(rotten)
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= nr < len_r and 0 <= nc < len_c and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            if fresh == 0:
                return ans
        
        return -1