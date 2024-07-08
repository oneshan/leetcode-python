# 0976 - Minimum Area Rectangle
# Date: 2024-05-26
# Runtime: 1803 ms, Memory: 16.8 MB
# Submission Id: 1268345150


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        counter = Counter(tuple(point) for point in points)

        ans = float('inf')
        for x, y in counter:
            for xx, yy in counter:
                if x == xx or y == yy:
                    continue
                height, width = abs(y-yy), abs(x-xx)
                if (x, yy) in counter and (xx, y) in counter:
                    ans = min(ans, height * width)

        return ans if ans != float('inf') else 0