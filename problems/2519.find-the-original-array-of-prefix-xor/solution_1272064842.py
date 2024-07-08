# 2519 - Find The Original Array of Prefix Xor
# Date: 2024-05-30
# Runtime: 553 ms, Memory: 35.1 MB
# Submission Id: 1272064842


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        ans = [0] * n
        curr = 0
        for i in range(n):
            ans[i] = pref[i] ^ curr
            curr ^= ans[i]
        return ans