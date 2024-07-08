# 2375 - Minimum Obstacle Removal to Reach Corner
# Date: 2024-05-28
# Runtime: 2768 ms, Memory: 40.3 MB
# Submission Id: 1270152992


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])

        dp = [[float('inf')] * len_c for _ in range(len_r)]
        dp[0][0] = grid[0][0]
        queue = deque([(0, 0, 0)])  # cost, r, c

        while queue:
            cost, r, c = queue.popleft()
            if r == len_r-1 and c == len_c-1:
                return cost
            for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= nr < len_r and 0 <= nc < len_c and dp[nr][nc] == float('inf'):
                    if grid[nr][nc] == 0:
                        dp[nr][nc] = cost + 1
                        queue.appendleft((cost, nr, nc))
                    else:
                        dp[nr][nc] = cost
                        queue.append((cost+1, nr, nc))