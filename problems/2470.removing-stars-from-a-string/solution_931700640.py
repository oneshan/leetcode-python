# 2470 - Removing Stars From a String
# Date: 2023-04-11
# Runtime: 223 ms, Memory: 15.6 MB
# Submission Id: 931700640


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)