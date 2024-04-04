# 0159 - Longest Substring with At Most Two Distinct Characters
# Date: 2024-04-02
# Runtime: 212 ms, Memory: 17.1 MB
# Submission Id: 1220861787


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = defaultdict(int)
        ans, left = 0, -1
        for right, ch in enumerate(s):
            counter[ch] = right
            if len(counter) == 3:
                left = min(counter.values())
                counter.pop(s[left])
            ans = max(ans, right-left)
        return ans