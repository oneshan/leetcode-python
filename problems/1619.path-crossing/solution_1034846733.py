# 1619 - Path Crossing
# Date: 2023-08-29
# Runtime: 42 ms, Memory: 16.5 MB
# Submission Id: 1034846733


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = {(0, 0)}
        
        x, y = 0, 0
        for ch in path:
            if ch == 'N':
                y += 1
            elif ch == 'E':
                x += 1
            elif ch == 'W':
                x -= 1
            else:
                y -= 1
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False