# 0340 - Longest Substring with At Most K Distinct Characters
# Date: 2023-09-14
# Runtime: 68 ms, Memory: 16.6 MB
# Submission Id: 1048550514


from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        table = defaultdict(int)
        
        ans = left = 0
        for right, ch in enumerate(s):
            table[ch] += 1
            while len(table) > k:
                if table[s[left]] == 1:
                    table.pop(s[left])
                else:
                    table[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans