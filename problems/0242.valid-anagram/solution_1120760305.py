# 0242 - Valid Anagram
# Date: 2023-12-16
# Runtime: 58 ms, Memory: 16.8 MB
# Submission Id: 1120760305


from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = defaultdict(int)
        for ch_s, ch_t in zip(s, t):
            counter[ch_s] += 1
            counter[ch_t] -= 1
            
        return all(c == 0 for c in counter.values())