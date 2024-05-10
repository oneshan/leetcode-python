# 0424 - Longest Repeating Character Replacement
# Date: 2024-05-09
# Runtime: 98 ms, Memory: 16.6 MB
# Submission Id: 1253530930


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()

        ans = left = max_freq = 0
        for right, ch in enumerate(s):
            counter[ch] += 1
            length = right - left + 1
            max_freq = max(max_freq, counter[ch])
            if length - max_freq <= k:
                ans = max(ans, length)
            else:
                counter[s[left]] -= 1
                left += 1
        return ans