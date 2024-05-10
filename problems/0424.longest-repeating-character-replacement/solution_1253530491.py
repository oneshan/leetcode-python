# 0424 - Longest Repeating Character Replacement
# Date: 2024-05-09
# Runtime: 101 ms, Memory: 16.9 MB
# Submission Id: 1253530491


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()

        ans = left = 0
        for right, ch in enumerate(s):
            counter[ch] += 1
            length = right - left + 1
            if length - max(counter.values()) <= k:
                ans = max(ans, length)
            else:
                counter[s[left]] -= 1
                left += 1
        return ans