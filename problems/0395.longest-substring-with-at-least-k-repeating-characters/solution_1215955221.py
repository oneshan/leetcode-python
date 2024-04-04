# 0395 - Longest Substring with At Least K Repeating Characters
# Date: 2024-03-28
# Runtime: 44 ms, Memory: 16.6 MB
# Submission Id: 1215955221


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        counter = Counter(s)
        for ch in set(s):
            if counter[ch] < k:
                res = 0
                for t in s.split(ch):
                    res = max(res, self.longestSubstring(t, k))
                return res
        return len(s)
