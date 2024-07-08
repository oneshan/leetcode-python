# 2914 - Find the Safest Path in a Grid
# Date: 2024-05-15
# Runtime: 2451 ms, Memory: 25.6 MB
# Submission Id: 1258441262


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        if grid[0][0] or grid[-1][-1]:
            return 0

        thieves = [(r, c) for r in range(len_r) for c in range(len_c) if grid[r][c]]
        queue = deque(thieves)
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= nr < len_r and 0 <= nc < len_c and grid[nr][nc] == 0:
                        grid[nr][nc] = grid[r][c] + 1
                        queue.append((nr, nc))

        max_heap = [(-grid[0][0]+1, 0, 0)]
        grid[0][0] = -1

        while max_heap:
            dist, r, c = heapq.heappop(max_heap)
            if r == len_r - 1 and c == len_c - 1:
                return -dist            
            for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= nr < len_r and 0 <= nc < len_c and grid[nr][nc] != -1:
                    next_dist = min(-dist, grid[nr][nc]-1)
                    grid[nr][nc] = -1
                    heapq.heappush(max_heap, (-next_dist, nr, nc))

        return 0