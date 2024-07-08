# 3396 - Valid Word
# Date: 2024-05-21
# Runtime: 30 ms, Memory: 16.6 MB
# Submission Id: 1263728424


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        has_vowel = has_consonant = False
        for ch in word.lower():
            if not ch.isalnum():
                return False
            if 0 <= ord(ch) - ord('a') < 26:
                if ch in {'a', 'e', 'i', 'o', 'u'}:
                    has_vowel = True
                else:
                    has_consonant = True
        return has_vowel and has_consonant