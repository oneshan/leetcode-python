# 3057 - Count K-Subsequences of a String With Maximum Beauty
# Date: 2023-11-08
# Runtime: 79 ms, Memory: 18.6 MB
# Submission Id: 1094414810


from collections import Counter
from math import comb

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 1_000_000_007
        counter = Counter(s)
        if k > len(counter):
            return 0
        
        arr = sorted(counter.values(), reverse=True)
        ans = 1
        for i in range(k):
            ans = (ans * arr[i]) % MOD
        
        last, n = arr[k-1], len(arr)
        c1 = sum(arr[i] == arr[k-1] for i in range(k))
        c2 = sum(arr[i] == arr[k-1] for i in range(n))
        ans = (ans * comb(c2, c1)) % MOD

        return ans