# 0916 - Decoded String at Index
# Date: 2023-09-27
# Runtime: 34 ms, Memory: 16.3 MB
# Submission Id: 1060284778


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = [0]
        num = 0
        for ch in s:
            if ch.isdigit():
                length = stack[-1] * int(ch)
                stack.append(length)
            else:
                length = stack[-1] + 1
                stack.append(length)
                
        size = len(stack)
        while stack:
            k %= stack[-1]
            size -= 1
            if k == 0 and s[size-1].isalpha():
                return s[size-1]
            stack.pop()
        return ""
