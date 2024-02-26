# 2243 - Check if All A's Appears Before All B's
# Date: 2023-07-28
# Runtime: 44 ms, Memory: 16.3 MB
# Submission Id: 1006186030


class Solution:
    def checkString(self, s: str) -> bool:
        prev_b = False
        for ch in s:
            if ch == 'b':
                prev_b = True
            elif prev_b:
                return False
        return True