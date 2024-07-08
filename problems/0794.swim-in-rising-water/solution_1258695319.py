# 0794 - Swim in Rising Water
# Date: 2024-05-15
# Runtime: 78 ms, Memory: 17.3 MB
# Submission Id: 1258695319


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        min_heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        while min_heap:
            time, r, c = heapq.heappop(min_heap)
            if r == len_r - 1 and c == len_c - 1:
                return time
            for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= nr < len_r and 0 <= nc < len_c and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    next_time = max(time, grid[nr][nc])
                    heapq.heappush(min_heap, (next_time, nr, nc))