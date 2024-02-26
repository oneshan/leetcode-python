# 0567 - Permutation in String
# Date: 2023-02-04
# Runtime: 73 ms, Memory: 14 MB
# Submission Id: 891034068


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26
        for ch in s1:
            freq1[ord(ch)-ord('a')] += 1
        
        n1 = len(s1)
        ans = []
        for idx, ch in enumerate(s2):
            freq2[ord(ch)-ord('a')] += 1
            if idx >= n1:
                old_ch = ord(s2[idx-n1]) - ord('a')
                freq2[old_ch] -= 1
            if freq1 == freq2:
                return True
        return False