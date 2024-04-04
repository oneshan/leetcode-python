# 0159 - Longest Substring with At Most Two Distinct Characters
# Date: 2024-04-02
# Runtime: 279 ms, Memory: 17.2 MB
# Submission Id: 1220857671


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = defaultdict(int)
        ans = left = 0
        for right, ch in enumerate(s):
            counter[ch] += 1
            while len(counter) > 2:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    counter.pop(s[left])
                left += 1
            ans = max(ans, right-left+1)
        return ans