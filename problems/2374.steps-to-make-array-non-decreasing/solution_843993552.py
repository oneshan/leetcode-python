# 2374 - Steps to Make Array Non-decreasing
# Date: 2022-11-16
# Runtime: 3298 ms, Memory: 28.5 MB
# Submission Id: 843993552


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for num in nums:
            step = 0
            while stack and stack[-1][0] <= num:
                step = max(step, stack.pop()[1])
            step = step+1 if stack else 0
            stack.append([num, step])
            ans = max(ans, step)
        return ans