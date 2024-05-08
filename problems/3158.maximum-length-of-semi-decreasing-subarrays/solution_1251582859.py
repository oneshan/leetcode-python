# 3158 - Maximum Length of Semi-Decreasing Subarrays
# Date: 2024-05-07
# Runtime: 423 ms, Memory: 31.5 MB
# Submission Id: 1251582859


class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        n = len(nums)

        stack = []
        for i in range(n-1, -1, -1):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        ans = 0
        curr_max = float('-inf')
        for left in range(n):
            if left >= stack[-1]:
                stack.pop()
            if nums[left] > curr_max:
                curr_max = nums[left]
                while stack and nums[left] > nums[stack[-1]]:
                    right = stack.pop()
                    ans = max(ans, right - left + 1)
            if not stack:
                break

        return ans