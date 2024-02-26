# 0223 - Rectangle Area
# Date: 2022-10-15
# Runtime: 103 ms, Memory: 14 MB
# Submission Id: 822947056


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        dx = min(ax2, bx2) - max(ax1, bx1)
        dy = min(ay2, by2) - max(ay1, by1)
        
        overlap_area = dx * dy if dx > 0 and dy > 0 else 0
        area_a = (ax2-ax1) * (ay2-ay1)
        area_b = (bx2-bx1) * (by2-by1)
        return area_a + area_b - overlap_area