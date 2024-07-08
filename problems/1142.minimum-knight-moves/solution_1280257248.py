# 1142 - Minimum Knight Moves
# Date: 2024-06-07
# Runtime: 3282 ms, Memory: 78.4 MB
# Submission Id: 1280257248


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == y == 0:
            return 0

        directions = [(-2,1), (-1,2), (1,2), (2,1),
                      (-2,-1), (-1,-2), (1,-2), (2,-1)]

        seen = {(0, 0)}
        queue = deque([(0,0)])
        step = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == x and c == y:
                    return step
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr, nc) in seen:
                        continue
                    seen.add((nr, nc))
                    queue.append((nr, nc))

            step += 1

        return -1