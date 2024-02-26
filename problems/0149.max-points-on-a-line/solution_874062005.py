# 0149 - Max Points on a Line
# Date: 2023-01-08
# Runtime: 118 ms, Memory: 14 MB
# Submission Id: 874062005


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return n

        ans = 0
        for i in range(n):
            slope = {}
            count_dup = count_inf = 0

            for j in range(i, n):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx == 0 and dy == 0:
                    count_dup += 1
                if dx == 0:
                    count_inf += 1
                else:
                    tmp = self.gcd(dx, dy)
                    s = (dx // tmp, dy // tmp)
                    slope[s] = slope.get(s, 0) + 1

            ans = max(ans, count_inf)
            for s in slope:
                ans = max(ans, slope[s] + count_dup)

        return ans
    
    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x % y)