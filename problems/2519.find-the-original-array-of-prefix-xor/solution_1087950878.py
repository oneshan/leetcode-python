# 2519 - Find The Original Array of Prefix Xor
# Date: 2023-10-31
# Runtime: 664 ms, Memory: 36.4 MB
# Submission Id: 1087950878


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        ans = [0] * n
        ans[0] = pref[0]
        for i in range(1, n):
            ans[i] = pref[i-1] ^ pref[i]
        return ans