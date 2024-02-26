# 1915 - Check if One String Swap Can Make Strings Equal
# Date: 2022-05-30
# Runtime: 59 ms, Memory: 14 MB
# Submission Id: 710506142


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        count = 0
        swap_idx = -1
        for idx in range(len(s1)):
            if s1[idx] == s2[idx]:
                continue
            if count:
                if s1[idx] != s2[swap_idx] or s1[swap_idx] != s2[idx]:
                    return False
            if count > 2:
                return False
            count += 1
            swap_idx = idx
        return count in (0, 2)