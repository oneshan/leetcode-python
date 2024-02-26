# 0976 - Minimum Area Rectangle
# Date: 2023-10-28
# Runtime: 928 ms, Memory: 16.5 MB
# Submission Id: 1086013154


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        ans = float('inf')
        
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    ans = min(ans, abs((x1-x2)*(y1-y2)))
            seen.add((x1, y1))
        
        return ans if ans != float('inf') else 0