# 0567 - Permutation in String
# Date: 2023-08-30
# Runtime: 52 ms, Memory: 16.5 MB
# Submission Id: 1036082219


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        freq_1 = [0] * 26
        freq_2 = [0] * 26
        
        for idx in range(n1):
            freq_1[ord(s1[idx])-ord('a')] += 1
            freq_2[ord(s2[idx])-ord('a')] += 1
            
        for idx in range(n1, n2):
            if freq_1 == freq_2:
                return True
            freq_2[ord(s2[idx])-ord('a')] += 1
            freq_2[ord(s2[idx-n1]) - ord('a')] -= 1
        return freq_1 == freq_2