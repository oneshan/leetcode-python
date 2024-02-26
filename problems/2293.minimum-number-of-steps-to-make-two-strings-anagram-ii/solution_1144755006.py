# 2293 - Minimum Number of Steps to Make Two Strings Anagram II
# Date: 2024-01-13
# Runtime: 178 ms, Memory: 19.8 MB
# Submission Id: 1144755006


from collections import defaultdict

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        
        ans = 0
        for i in range(26):
            ch = chr(ord('a')+i)
            ans += abs(c1[ch]-c2[ch])
        return ans