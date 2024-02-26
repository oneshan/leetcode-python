# 2427 - First Letter to Appear Twice
# Date: 2022-09-26
# Runtime: 66 ms, Memory: 13.8 MB
# Submission Id: 809103101


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = 0
        for ch in s:
            mask_bit = 1 << (ord(ch) - 97)
            if seen & mask_bit:
                return ch
            seen |= mask_bit            