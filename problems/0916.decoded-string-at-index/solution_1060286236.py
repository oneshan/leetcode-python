# 0916 - Decoded String at Index
# Date: 2023-09-27
# Runtime: 28 ms, Memory: 16.2 MB
# Submission Id: 1060286236


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1
        
        for ch in reversed(s):
            k %= size
            if k == 0 and ch.isalpha():
                return ch
            
            if ch.isdigit():
                size /= int(ch)
            else:
                size -= 1
        return ""
