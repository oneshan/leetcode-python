# 2519 - Find The Original Array of Prefix Xor
# Date: 2023-10-31
# Runtime: 675 ms, Memory: 31.3 MB
# Submission Id: 1087955563


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        for i in range(n-1, 0, -1):
            pref[i] ^= pref[i-1]
        return pref