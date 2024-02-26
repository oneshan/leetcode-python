# 0520 - Detect Capital
# Date: 2023-01-30
# Runtime: 38 ms, Memory: 13.7 MB
# Submission Id: 887987887


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        n = len(word)
        if n == 1:
            return True
        
        # case 1
        if word[0].isupper() and word[1].isupper():
            for i in range(2, n):
                if word[i].islower():
                    return False
        # case 2, 3
        else:
            for i in range(1, n):
                if word[i].isupper():
                    return False
        
        return True