# 0042 - Trapping Rain Water
# Date: 2024-03-08
# Runtime: 102 ms, Memory: 18.4 MB
# Submission Id: 1197598656


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0

        max_left, max_right = height[left], height[right]
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                ans += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                ans += max_right - height[right]

        return ans