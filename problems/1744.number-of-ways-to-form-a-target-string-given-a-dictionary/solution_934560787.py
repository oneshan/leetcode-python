# 1744 - Number of Ways to Form a Target String Given a Dictionary
# Date: 2023-04-16
# Runtime: 2713 ms, Memory: 298.7 MB
# Submission Id: 934560787


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        len_t = len(target)
        len_w = len(words[0])
        
        count = [[0] * 26 for _ in range(len_w)]
        for word in words:
            for idx, ch in enumerate(word):
                count[idx][ord(ch) - ord('a')] += 1
        
        @cache
        def recur(iw, it):
            if it == len_t:
                return 1
            if iw >= len_w:
                return 0
            return count[iw][ord(target[it])-ord('a')] * recur(iw+1, it+1) + recur(iw+1, it)
        
        return recur(0, 0) % mod