# 1349 - Check If It Is a Straight Line
# Date: 2023-06-05
# Runtime: 87 ms, Memory: 16.9 MB
# Submission Id: 964050171


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        for x, y in coordinates:
            if (x2-x1) * (y-y1) != (x-x1) * (y2-y1):
                return False
        return True