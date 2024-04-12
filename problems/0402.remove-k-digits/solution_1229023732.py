# 0402 - Remove K Digits
# Date: 2024-04-11
# Runtime: 57 ms, Memory: 17.9 MB
# Submission Id: 1229023732


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)

        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        j = len(stack) - k

        if i >= j:
            return '0'
        return ''.join(stack[i:j])