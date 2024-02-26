# 0242 - Valid Anagram
# Date: 2024-02-09
# Runtime: 46 ms, Memory: 17.1 MB
# Submission Id: 1170247701


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = Counter(s)
        for ch in t:
            counter[ch] -= 1
            if counter[ch] < 0:
                return False
        return True