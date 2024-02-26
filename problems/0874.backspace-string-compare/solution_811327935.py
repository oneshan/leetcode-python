# 0874 - Backspace String Compare
# Date: 2022-09-29
# Runtime: 65 ms, Memory: 13.9 MB
# Submission Id: 811327935


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        result_s = []
        result_t = []
        
        for ch in s:
            if ch == '#':
                if result_s:
                    result_s.pop()
            else:
                result_s.append(ch)
        
        for ch in t:
            if ch == '#':
                if result_t:
                    result_t.pop()
            else:
                result_t.append(ch)
        
        return result_s == result_t