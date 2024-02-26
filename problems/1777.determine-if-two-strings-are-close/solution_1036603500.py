# 1777 - Determine if Two Strings Are Close
# Date: 2023-08-31
# Runtime: 121 ms, Memory: 17.9 MB
# Submission Id: 1036603500


from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        return counter1.keys() == counter2.keys() and Counter(counter1.values()) == Counter(counter2.values())