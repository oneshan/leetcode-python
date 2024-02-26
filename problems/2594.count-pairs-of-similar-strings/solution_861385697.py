# 2594 - Count Pairs Of Similar Strings
# Date: 2022-12-18
# Runtime: 98 ms, Memory: 14.1 MB
# Submission Id: 861385697


from collections import defaultdict

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        counter = defaultdict(int)
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            counter[mask] += 1
        
        ans = 0
        for count in counter.values():
            ans += count * (count-1) // 2
        return ans