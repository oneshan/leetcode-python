# 0402 - Remove K Digits
# Date: 2023-09-24
# Runtime: 46 ms, Memory: 17.8 MB
# Submission Id: 1057945252


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = []
        
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        j = n if k == 0 else -k

        return ''.join(stack[i:j]) or '0'
