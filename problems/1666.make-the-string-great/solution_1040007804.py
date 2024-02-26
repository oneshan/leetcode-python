# 1666 - Make The String Great
# Date: 2023-09-04
# Runtime: 36 ms, Memory: 16.3 MB
# Submission Id: 1040007804


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)