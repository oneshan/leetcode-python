# 2375 - Minimum Obstacle Removal to Reach Corner
# Date: 2024-05-28
# Runtime: 2394 ms, Memory: 40.7 MB
# Submission Id: 1270148052


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])

        dp = [[float('inf')] * len_c for _ in range(len_r)]
        dp[0][0] = grid[0][0]
        heap = [(0, 0, 0)]  # cost, r, c

        while heap:
            cost, r, c = heapq.heappop(heap)
            if dp[r][c] < cost:
                continue
            for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= nr < len_r and 0 <= nc < len_c and cost + grid[nr][nc] < dp[nr][nc]:
                    dp[nr][nc] = cost + grid[nr][nc]
                    heapq.heappush(heap, (dp[nr][nc], nr, nc))

        return dp[-1][-1]