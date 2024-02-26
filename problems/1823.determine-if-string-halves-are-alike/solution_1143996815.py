# 1823 - Determine if String Halves Are Alike
# Date: 2024-01-12
# Runtime: 34 ms, Memory: 17.4 MB
# Submission Id: 1143996815


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        half = len(s) // 2
        count = 0
        
        for i in range(half):
            if s[i] in vowels:
                count += 1
            if s[i+half] in vowels:
                count -= 1
        return count == 0