# 2186 - Count Vowel Substrings of a String
# Date: 2024-03-31
# Runtime: 35 ms, Memory: 16.4 MB
# Submission Id: 1218954058


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans, left = 0, -1
        last_seen = {vowel: -1 for vowel in 'aeiou'}
        for idx, ch in enumerate(word):
            if ch in last_seen:
                last_seen[ch] = idx
            else:
                left = idx
            ans += max(0, min(last_seen.values()) - left)
        return ans