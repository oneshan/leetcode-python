# 1666 - Make The String Great
# Date: 2022-09-29
# Runtime: 80 ms, Memory: 14 MB
# Submission Id: 811413331


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        case_diff = ord('a') - ord('A')
        for ch in s:
            if stack and abs(ord(stack[-1])-ord(ch)) == case_diff:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)