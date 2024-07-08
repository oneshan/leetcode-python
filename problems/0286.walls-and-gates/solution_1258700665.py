# 0286 - Walls and Gates
# Date: 2024-05-15
# Runtime: 170 ms, Memory: 19.4 MB
# Submission Id: 1258700665


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        len_r, len_c = len(rooms), len(rooms[0])
        INF = 2147483647
        queue = deque()
        for r in range(len_r):
            for c in range(len_c):
                if rooms[r][c] == 0:
                    queue.append((r, c, 0))

        while queue:
            r, c, dist = queue.popleft()
            for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= nr < len_r and 0 <= nc < len_c and rooms[nr][nc] == INF:
                    rooms[nr][nc] = dist + 1
                    queue.append((nr, nc, rooms[nr][nc]))