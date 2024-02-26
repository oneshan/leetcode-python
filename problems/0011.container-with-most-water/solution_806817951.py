# 0011 - Container With Most Water
# Date: 2022-09-23
# Runtime: 799 ms, Memory: 27.5 MB
# Submission Id: 806817951


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_water = 0
        while left < right:
            max_water = max(max_water, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left +=1
            else:
                right -= 1
        return max_water