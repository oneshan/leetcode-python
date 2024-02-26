# 0567 - Permutation in String
# Date: 2023-08-30
# Runtime: 58 ms, Memory: 16.5 MB
# Submission Id: 1036078605


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_1 = [0] * 26
        freq_2 = [0] * 26
        
        for ch in s1:
            freq_1[ord(ch)-ord('a')] += 1
        
        n1 = len(s1)
        for idx, ch in enumerate(s2):
            freq_2[ord(ch)-ord('a')] += 1
            if idx >= n1:
                freq_2[ord(s2[idx-n1]) - ord('a')] -= 1
            if freq_1 == freq_2:
                return True
        return False