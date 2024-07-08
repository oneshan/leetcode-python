# 1753 - Path With Minimum Effort
# Date: 2024-05-15
# Runtime: 551 ms, Memory: 18.6 MB
# Submission Id: 1258449937


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        len_r, len_c = len(heights), len(heights[0])

        min_heap = [(0, 0, 0)]
        seen = {(0, 0): 0}

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)
            if r == len_r-1 and c == len_c-1:
                return effort
            for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= nr < len_r and 0 <= nc < len_c:
                    next_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if seen.get((nr, nc), float('inf')) <= next_effort:
                        continue
                    seen[(nr, nc)] = next_effort
                    heapq.heappush(min_heap, (next_effort, nr, nc))