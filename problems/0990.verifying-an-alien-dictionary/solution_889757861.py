# 0990 - Verifying an Alien Dictionary
# Date: 2023-02-02
# Runtime: 44 ms, Memory: 14 MB
# Submission Id: 889757861


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = {ch: idx for idx, ch in enumerate(order)}
        n = len(words)
                
        def compare(w1, w2):
            for c1, c2 in zip(w1, w2):
                if table[c1] < table[c2]:
                    return True
                if table[c1] > table[c2]:
                    return False
            return len(w1) <= len(w2)
        
        for i in range(1, n):
            if not compare(words[i-1], words[i]):
                return False
        return True