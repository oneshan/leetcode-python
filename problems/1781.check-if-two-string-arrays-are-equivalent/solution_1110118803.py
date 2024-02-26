# 1781 - Check If Two String Arrays are Equivalent
# Date: 2023-12-01
# Runtime: 39 ms, Memory: 16.4 MB
# Submission Id: 1110118803


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        def get_ch(arr):
            for word in arr:
                for ch in word:
                    yield ch
            yield None
        
        gen1 = get_ch(word1)
        gen2 = get_ch(word2)
        c1, c2 = next(gen1), next(gen2)
        while c1 and c2:
            if c1 != c2:
                return False
            c1, c2 = next(gen1), next(gen2)        
        
        return c1 is None and c2 is None