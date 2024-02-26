# 3056 - Determine if a Cell Is Reachable at a Given Time
# Date: 2023-09-10
# Runtime: 44 ms, Memory: 16.2 MB
# Submission Id: 1045215440


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx, dy = fx-sx, fy-sy
        
        if dx == dy == 0:
            return t != 1
        
        min_dist = max(abs(dx), abs(dy))
        return min_dist <= t