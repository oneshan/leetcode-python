# 1501 - Circle and Rectangle Overlapping
# Date: 2023-10-28
# Runtime: 50 ms, Memory: 16.4 MB
# Submission Id: 1085890304


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearest_x = max(x1, min(xCenter, x2))
        nearest_y = max(y1, min(yCenter, y2))
        return (nearest_x - xCenter) ** 2 + (nearest_y - yCenter) ** 2 <= radius ** 2