# 1666 - Make The String Great
# Date: 2024-04-05
# Runtime: 32 ms, Memory: 16.6 MB
# Submission Id: 1223767096


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] != ch and stack[-1] in (ch.upper(), ch.lower()):
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)