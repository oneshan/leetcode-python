# 0983 - Validate Stack Sequences
# Date: 2023-04-13
# Runtime: 77 ms, Memory: 14.2 MB
# Submission Id: 932783022


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        idx = 0
        n = len(popped)
        stack = []
        for val in pushed:
            stack.append(val)
            while idx < n and stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        return idx == len(popped)