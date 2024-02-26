# 0042 - Trapping Rain Water
# Date: 2022-10-30
# Runtime: 270 ms, Memory: 16 MB
# Submission Id: 833348801


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]
        
        ans = 0
        while left < right:
            if height[left] < height[right]:
                ans += max_left - height[left]
                left += 1
                max_left = max(max_left, height[left])
            else:
                ans += max_right - height[right]
                right -= 1
                max_right = max(max_right, height[right])
        return ans    