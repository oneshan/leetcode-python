# 1960 - Check if the Sentence Is Pangram
# Date: 2022-09-26
# Runtime: 56 ms, Memory: 14 MB
# Submission Id: 809105724


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = 0
        full = (1 << 26) - 1
        for ch in sentence:
            mask_bit = 1 << (ord(ch) - 97)
            alpha |= mask_bit
            if alpha == full:
                return True
        return False