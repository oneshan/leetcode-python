# 0340 - Longest Substring with At Most K Distinct Characters
# Date: 2023-09-14
# Runtime: 66 ms, Memory: 16.5 MB
# Submission Id: 1048555622


from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        table = defaultdict(int)
        
        ans = 0
        for right in range(len(s)):
            table[s[right]] += 1
            if len(table) <= k:
                ans += 1
            elif table[s[right-ans]] == 1:
                table.pop(s[right-ans])
            else:
                table[s[right-ans]] -= 1
        return ans