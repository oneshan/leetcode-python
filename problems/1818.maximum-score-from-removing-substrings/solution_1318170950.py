# 1818 - Maximum Score From Removing Substrings
# Date: 2024-07-12
# Runtime: 224 ms, Memory: 18.2 MB
# Submission Id: 1318170950


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = 'a', 'b'
        if x < y:
            x, y, a, b = y, x, 'b', 'a'

        ans = 0
        for c1, c2, score in (a, b, x), (b, a, y):
            stack = []
            for ch in s:
                if stack and stack[-1] == c1 and ch == c2:
                    stack.pop()
                    ans += score
                else:
                    stack.append(ch)
            s = stack
        
        return ans