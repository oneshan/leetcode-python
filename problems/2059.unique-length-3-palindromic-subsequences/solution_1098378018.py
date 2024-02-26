# 2059 - Unique Length-3 Palindromic Subsequences
# Date: 2023-11-14
# Runtime: 743 ms, Memory: 17.3 MB
# Submission Id: 1098378018


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        
        for idx, ch in enumerate(s):
            num = ord(ch) - ord('a')
            if first[num] == -1:
                first[num] = idx
            last[num] = idx
            
        ans = 0
        for i in range(26):
            if first[i] == -1:
                continue
            middle = set()
            for j in range(first[i]+1, last[i]):
                middle.add(s[j])
            ans += len(middle)

        return ans