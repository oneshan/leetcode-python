# 0866 - Rectangle Overlap
# Date: 2022-10-15
# Runtime: 55 ms, Memory: 14 MB
# Submission Id: 822945445


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        dx = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        dy = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        return dx > 0 and dy > 0