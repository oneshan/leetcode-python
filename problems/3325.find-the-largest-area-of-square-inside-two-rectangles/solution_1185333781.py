# 3325 - Find the Largest Area of Square Inside Two Rectangles
# Date: 2024-02-25
# Runtime: 5408 ms, Memory: 17.4 MB
# Submission Id: 1185333781


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                o_x2 = min(topRight[i][0], topRight[j][0])
                o_x1 = max(bottomLeft[i][0], bottomLeft[j][0])
                o_y2 = min(topRight[i][1], topRight[j][1])
                o_y1 = max(bottomLeft[i][1], bottomLeft[j][1])
                
                if o_x2 > o_x1 and o_y2 > o_y1:
                    side = min(o_x2 - o_x1, o_y2 - o_y1)
                    ans = max(ans, side * side)
        return ans