# 1915 - Check if One String Swap Can Make Strings Equal
# Date: 2022-11-12
# Runtime: 34 ms, Memory: 13.7 MB
# Submission Id: 841710303


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap_idx = count = 0
        for idx in range(len(s1)):
            if s1[idx] == s2[idx]:
                continue
            if count > 1:
                return False
            if count and not (s1[swap_idx] == s2[idx] and s1[idx] == s2[swap_idx]):
                return False
            count += 1
            swap_idx = idx

        return count in (0, 2)