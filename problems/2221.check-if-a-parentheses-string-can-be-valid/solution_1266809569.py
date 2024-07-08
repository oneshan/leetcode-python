# 2221 - Check if a Parentheses String Can Be Valid
# Date: 2024-05-25
# Runtime: 110 ms, Memory: 21.1 MB
# Submission Id: 1266809569


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1:
            return False

        stack = []
        star = []

        for idx, ch in enumerate(s):
            if locked[idx] == '0':
                star.append(idx)
            elif ch == '(':
                stack.append(idx)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while stack:
            if not star or stack.pop() > star.pop():
                return False

        return True