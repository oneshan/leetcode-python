# 1567 - Maximum Number of Vowels in a Substring of Given Length
# Date: 2023-08-17
# Runtime: 140 ms, Memory: 17.1 MB
# Submission Id: 1023785150


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        ans = left = curr = 0
        for right in range(n):
            if s[right] in 'aeiou':
                curr += 1
            if right >= k and s[right-k] in 'aeiou':
                curr -= 1
            ans = max(ans, curr)
        return ans
                