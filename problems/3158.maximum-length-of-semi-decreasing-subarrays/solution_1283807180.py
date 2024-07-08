# 3158 - Maximum Length of Semi-Decreasing Subarrays
# Date: 2024-06-10
# Runtime: 423 ms, Memory: 31.7 MB
# Submission Id: 1283807180


class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        n = len(nums)
        stack = [] # mono increasing

        for i in range(n):
            if not stack or nums[i] > nums[stack[-1]]:
                stack.append(i)

        ans = 0
        for right in range(n-1, -1, -1):
            while stack and nums[stack[-1]] > nums[right]:
                left = stack.pop()
                ans = max(ans, right - left + 1)
        return ans