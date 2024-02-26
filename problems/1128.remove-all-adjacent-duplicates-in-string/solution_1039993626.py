# 1128 - Remove All Adjacent Duplicates In String
# Date: 2023-09-04
# Runtime: 69 ms, Memory: 17.1 MB
# Submission Id: 1039993626


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)