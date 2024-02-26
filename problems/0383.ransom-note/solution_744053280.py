# 0383 - Ransom Note
# Date: 2022-07-11
# Runtime: 151 ms, Memory: 14.1 MB
# Submission Id: 744053280


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = {}
        for ch in magazine:
            table[ch] = table.get(ch, 0) + 1
        
        for ch in ransomNote:
            if not table.get(ch):
                return False
            table[ch] -= 1
        return True