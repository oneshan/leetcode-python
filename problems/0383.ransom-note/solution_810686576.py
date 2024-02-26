# 0383 - Ransom Note
# Date: 2022-09-29
# Runtime: 129 ms, Memory: 14.1 MB
# Submission Id: 810686576


from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        words = defaultdict(int)
        for ch in magazine:
            words[ch] += 1
            
        for ch in ransomNote:
            words[ch] -= 1
            if words[ch] < 0:
                return False
        return True
        