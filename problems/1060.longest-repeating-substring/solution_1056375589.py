# 1060 - Longest Repeating Substring
# Date: 2023-09-22
# Runtime: 1164 ms, Memory: 238 MB
# Submission Id: 1056375589


from collections import defaultdict

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        table = defaultdict(int)
        n = len(s)
        
        for i in range(n):
            for j in range(i+1, n+1):
                table[s[i:j]] += 1
        
        sub_len = 0
        for sub, count in table.items():
            if count >= 2:
                sub_len = max(sub_len, len(sub))        
        return sub_len