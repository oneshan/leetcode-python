# 0438 - Find All Anagrams in a String
# Date: 2023-02-05
# Runtime: 99 ms, Memory: 15.1 MB
# Submission Id: 891940876


from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []
        
        ans = []
        pattern_p = [0] * 26
        pattern_s = [0] * 26
        for ch in p:
            pattern_p[ord(ch)-97] += 1
            
        for i in range(len_s):
            pattern_s[ord(s[i])-97] += 1
            if i >= len_p:
                pattern_s[ord(s[i-len_p])-97] -= 1
            if pattern_p == pattern_s:
                ans.append(i-len_p+1)
        return ans