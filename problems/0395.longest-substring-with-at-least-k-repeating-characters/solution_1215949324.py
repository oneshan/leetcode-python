# 0395 - Longest Substring with At Least K Repeating Characters
# Date: 2024-03-28
# Runtime: 149 ms, Memory: 16.6 MB
# Submission Id: 1215949324


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for count in range(1, 27):
            left = 0
            counter = Counter()
            for right, ch in enumerate(s):
                counter[ch] += 1
                while len(counter) > count:
                    counter[s[left]] -= 1
                    if counter[s[left]] == 0:
                        counter.pop(s[left])
                    left += 1
                if min(counter.values()) >= k:
                    ans = max(ans, right - left + 1)
        return ans