# 0874 - Backspace String Compare
# Date: 2022-07-23
# Runtime: 39 ms, Memory: 13.9 MB
# Submission Id: 754522185


from itertools import zip_longest

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def find_prev_ch(string):
            skip = 0
            for ch in reversed(string):
                if ch == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield ch
                    
        for ch_s, ch_t in zip_longest(find_prev_ch(s), find_prev_ch(t)):
            if ch_s != ch_t:
                return False
        return True