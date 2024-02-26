# 1781 - Check If Two String Arrays are Equivalent
# Date: 2023-12-01
# Runtime: 36 ms, Memory: 16.3 MB
# Submission Id: 1110119196


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        def get_ch(arr):
            for word in arr:
                for ch in word:
                    yield ch
            yield None
        
        return all(c1 == c2 for c1, c2 in zip(get_ch(word1), get_ch(word2)))