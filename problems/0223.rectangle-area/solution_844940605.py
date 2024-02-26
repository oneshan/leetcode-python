# 0223 - Rectangle Area
# Date: 2022-11-17
# Runtime: 126 ms, Memory: 14 MB
# Submission Id: 844940605


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        total = area1 + area2

        o_x2 = min(bx2, ax2)
        o_x1 = max(ax1, bx1)
        o_y2 = min(by2, ay2)
        o_y1 = max(ay1, by1)
    
        if o_x2 > o_x1 and o_y2 > o_y1:
            total -= (o_x2 - o_x1) * (o_y2 - o_y1)
        return total        