# 2374 - Steps to Make Array Non-decreasing
# Date: 2022-11-16
# Runtime: 2408 ms, Memory: 28.4 MB
# Submission Id: 844003852


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        stack = []
        for idx in range(n):
            cur = 0
            while stack and nums[idx] >= nums[stack[-1]]:
                cur = max(cur, dp[stack.pop()])
            if stack:
                dp[idx] = cur + 1
            stack.append(idx)
        return max(dp)