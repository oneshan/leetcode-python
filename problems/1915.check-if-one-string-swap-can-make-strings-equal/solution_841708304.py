# 1915 - Check if One String Swap Can Make Strings Equal
# Date: 2022-11-12
# Runtime: 49 ms, Memory: 14 MB
# Submission Id: 841708304


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if len(diff) == 2:
                    return False
                diff.append((c1, c2))

        if not diff:
            return True
        if len(diff) == 1:
            return False
        return diff[1][0] == diff[0][1] and diff[1][1] == diff[0][0]