# 0149 - Max Points on a Line
# Date: 2024-02-13
# Runtime: 78 ms, Memory: 16.6 MB
# Submission Id: 1173861395


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)
        
        n = len(points)
        if n <= 1:
            return n
        
        ans = 0
        for i in range(n):
            slope = defaultdict(int)
            count_dup = count_inf = 0
            for j in range(i, n):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx == 0 and dy == 0:
                    count_dup += 1
                if dx == 0:
                    count_inf += 1
                else:
                    gcd_val = gcd(dx, dy)
                    s = (dx // gcd_val, dy // gcd_val)
                    slope[s] += 1

            ans = max(ans, count_inf)
            for s in slope:
                ans = max(ans, slope[s] + count_dup)
        return ans