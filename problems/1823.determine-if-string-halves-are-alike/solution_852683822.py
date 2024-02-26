# 1823 - Determine if String Halves Are Alike
# Date: 2022-12-01
# Runtime: 78 ms, Memory: 13.9 MB
# Submission Id: 852683822


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        n = len(s) >> 1
        
        count = 0
        for i in range(n):
            if s[i] in vowels:
                count += 1
            if s[i+n] in vowels:
                count -= 1
        return count == 0