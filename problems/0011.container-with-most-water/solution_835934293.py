# 0011 - Container With Most Water
# Date: 2022-11-03
# Runtime: 2166 ms, Memory: 26 MB
# Submission Id: 835934293


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