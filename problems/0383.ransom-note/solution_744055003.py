# 0383 - Ransom Note
# Date: 2022-07-11
# Runtime: 91 ms, Memory: 14.2 MB
# Submission Id: 744055003


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        letter = {}
        for ch in magazine:
            letter[ch] = letter.get(ch, 0) + 1
        
        for ch in ransomNote:
            if not letter.get(ch):
                return False
            letter[ch] -= 1
        return True