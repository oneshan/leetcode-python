# 0011 - Container With Most Water
# Date: 2023-10-09
# Runtime: 610 ms, Memory: 29.2 MB
# Submission Id: 1070996331


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        while left < right:
            water = min(height[left], height[right]) * (right-left)
            ans = max(ans, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans