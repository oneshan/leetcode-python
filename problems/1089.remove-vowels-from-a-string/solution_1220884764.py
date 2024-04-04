# 1089 - Remove Vowels from a String
# Date: 2024-04-02
# Runtime: 40 ms, Memory: 16.6 MB
# Submission Id: 1220884764


class Solution:
    def removeVowels(self, s: str) -> str:
        return ''.join(ch for ch in s if ch not in {'a', 'e', 'i', 'o', 'u'})