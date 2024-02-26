# 0866 - Rectangle Overlap
# Date: 2022-10-15
# Runtime: 60 ms, Memory: 13.8 MB
# Submission Id: 822939292


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0]
                    or rec1[0] >= rec2[2]
                    or rec1[3] <= rec2[1]
                    or rec1[1] >= rec2[3])