# 0042 - Trapping Rain Water
# Date: 2024-04-12
# Runtime: 85 ms, Memory: 18.4 MB
# Submission Id: 1229999251


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0

        max_left, max_right = height[left], height[right] 
        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
                
            if max_left < max_right:
                ans += max_left - height[left]
                left += 1
            else:
                ans += max_right - height[right]
                right -= 1

        return ans