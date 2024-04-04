# 3349 - Maximum Length Substring With Two Occurrences
# Date: 2024-03-24
# Runtime: 41 ms, Memory: 16.6 MB
# Submission Id: 1212110213


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        counter = defaultdict(int)
        
        ans = 0
        for right, ch in enumerate(s):
            counter[ch] += 1
            while counter[ch] > 2:
                counter[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans