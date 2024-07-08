# 0976 - Minimum Area Rectangle
# Date: 2024-05-26
# Runtime: 760 ms, Memory: 16.8 MB
# Submission Id: 1268347444


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        ans = float('inf')
        for x1, y1 in points:
            if (x1, y1) in seen:
                continue
            for (x2, y2) in seen:
                if x1 == x2 or y1 == y2:
                    continue
                height, width = abs(y2-y1), abs(x2-x1)
                if (x1, y2) in seen and (x2, y1) in seen:
                    ans = min(ans, height * width)
            seen.add((x1, y1))

        return ans if ans != float('inf') else 0