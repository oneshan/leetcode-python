# 0242 - Valid Anagram
# Date: 2022-11-03
# Runtime: 108 ms, Memory: 14.5 MB
# Submission Id: 835900390


from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = defaultdict(int)
        for ch in s:
            dict_s[ch] += 1
        
        for ch in t:
            dict_s[ch] -= 1
            if dict_s[ch] < 0:
                return False
        return True