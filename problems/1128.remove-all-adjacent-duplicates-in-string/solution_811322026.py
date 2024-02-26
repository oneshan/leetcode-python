# 1128 - Remove All Adjacent Duplicates In String
# Date: 2022-09-29
# Runtime: 115 ms, Memory: 14.8 MB
# Submission Id: 811322026


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)