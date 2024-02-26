# 3056 - Determine if a Cell Is Reachable at a Given Time
# Date: 2023-11-08
# Runtime: 38 ms, Memory: 16.2 MB
# Submission Id: 1094162599


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(sx - fx)
        dy = abs(sy - fy)
        
        if t == 1 and dx == dy == 0:
            return False
        return t >= max(dx, dy)