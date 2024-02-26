# 0149 - Max Points on a Line
# Date: 2024-02-13
# Runtime: 77 ms, Memory: 16.7 MB
# Submission Id: 1173865090


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:        
        n = len(points)
        if n <= 1:
            return n
        
        ans = 0
        for i in range(n):
            count = defaultdict(int)
            for j in range(n):
                if i == j:
                    continue
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                count[math.atan2(dy, dx)] += 1
            ans = max(ans, 1 + max(count.values()))
        return ans