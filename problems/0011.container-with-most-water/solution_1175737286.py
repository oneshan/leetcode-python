# 0011 - Container With Most Water
# Date: 2024-02-15
# Runtime: 536 ms, Memory: 29.5 MB
# Submission Id: 1175737286


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1

        ans = 0
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return ans
