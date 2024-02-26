# 0242 - Valid Anagram
# Date: 2022-10-18
# Runtime: 83 ms, Memory: 14.4 MB
# Submission Id: 825201120


from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = defaultdict(int)
        for i in range(len(s)):
            counter[s[i]] += 1
            counter[t[i]] -= 1
        return len(set(counter.values())) == 1