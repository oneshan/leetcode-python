# 1742 - Widest Vertical Area Between Two Points Containing No Points
# Date: 2023-12-21
# Runtime: 695 ms, Memory: 59.9 MB
# Submission Id: 1124737642


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = [x for x, y in points]
        arr.sort()
        
        ans = 0
        for i in range(1, len(arr)):
            ans = max(ans, arr[i]-arr[i-1])
        return ans