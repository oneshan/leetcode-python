# 1777 - Determine if Two Strings Are Close
# Date: 2022-12-03
# Runtime: 614 ms, Memory: 15.3 MB
# Submission Id: 853505993


from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        if len(c1) != len(c2):
            return False
        if set(c1) != set(c2):
            return False
        
        freq1 = Counter(c1.values())
        freq2 = Counter(c2.values())
        return freq1 == freq2