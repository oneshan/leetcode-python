# 0383 - Ransom Note
# Date: 2023-08-23
# Runtime: 59 ms, Memory: 16.4 MB
# Submission Id: 1029617890


from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        words = Counter(magazine)
            
        for ch in ransomNote:
            words[ch] -= 1
            if words[ch] < 0:
                return False
        return True
        