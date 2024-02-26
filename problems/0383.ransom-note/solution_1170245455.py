# 0383 - Ransom Note
# Date: 2024-02-09
# Runtime: 56 ms, Memory: 16.9 MB
# Submission Id: 1170245455


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_r = Counter(ransomNote)
        counter_m = Counter(magazine)

        for ch in counter_r:
            if counter_r[ch] > counter_m[ch]:
                return False
        return True