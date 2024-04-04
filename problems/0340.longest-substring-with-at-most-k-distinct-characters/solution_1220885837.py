# 0340 - Longest Substring with At Most K Distinct Characters
# Date: 2024-04-02
# Runtime: 70 ms, Memory: 16.8 MB
# Submission Id: 1220885837


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = left = 0
        counter = defaultdict(int)

        for right, ch in enumerate(s):
            counter[ch] += 1
            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    counter.pop(s[left])
                left += 1
            ans = max(ans, right-left+1)
        return ans