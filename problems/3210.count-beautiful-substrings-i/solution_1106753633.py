# 3210 - Count Beautiful Substrings I
# Date: 2023-11-26
# Runtime: 1153 ms, Memory: 16.3 MB
# Submission Id: 1106753633


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            vowels = consonants = 0
            for j in range(i, n):
                if s[j] in {'a', 'e', 'i', 'o', 'u'}:
                    vowels += 1
                else:
                    consonants += 1
                if vowels == consonants and vowels * consonants % k == 0:
                    ans += 1
        return ans