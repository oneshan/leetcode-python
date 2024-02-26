# 1770 - Minimum Deletions to Make Character Frequencies Unique
# Date: 2023-09-12
# Runtime: 122 ms, Memory: 17.2 MB
# Submission Id: 1047082841


from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        
        ans = 0
        seen_freq = set()
        for i in range(26):
            ch = chr(ord('a')+i)
            while freq[ch] and freq[ch] in seen_freq:
                freq[ch] -= 1
                ans += 1
            seen_freq.add(freq[ch])
        return ans