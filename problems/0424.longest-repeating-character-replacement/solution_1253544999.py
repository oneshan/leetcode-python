# 0424 - Longest Repeating Character Replacement
# Date: 2024-05-09
# Runtime: 102 ms, Memory: 16.7 MB
# Submission Id: 1253544999


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()

        ans = left = max_freq = 0
        for right, ch in enumerate(s):
            counter[ch] += 1
            max_freq = max(max_freq, counter[ch])
            while (right - left + 1) - max_freq > k:
                counter[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans