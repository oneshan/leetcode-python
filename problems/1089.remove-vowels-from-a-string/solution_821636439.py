# 1089 - Remove Vowels from a String
# Date: 2022-10-13
# Runtime: 51 ms, Memory: 13.8 MB
# Submission Id: 821636439


class Solution:
    def removeVowels(self, s: str) -> str:
        new_s = []
        for ch in s:
            if ch in 'aeiou':
                continue
            new_s.append(ch)
        return ''.join(new_s)