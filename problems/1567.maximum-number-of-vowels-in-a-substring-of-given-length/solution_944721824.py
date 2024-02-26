# 1567 - Maximum Number of Vowels in a Substring of Given Length
# Date: 2023-05-05
# Runtime: 190 ms, Memory: 17.4 MB
# Submission Id: 944721824


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = count = 0
        for idx, ch in enumerate(s):
            if ch in vowels:
                count += 1
            if idx >= k and s[idx-k] in vowels:
                count -= 1
            ans = max(ans, count)
        return ans