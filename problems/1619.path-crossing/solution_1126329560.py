# 1619 - Path Crossing
# Date: 2023-12-23
# Runtime: 38 ms, Memory: 17.4 MB
# Submission Id: 1126329560


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = {(0, 0)}
        x = y = 0
        for ch in path:
            if ch == 'N':
                y += 1
            elif ch == 'S':
                y -= 1
            elif ch == 'E':
                x += 1
            elif ch == 'W':
                x -= 1
            
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False