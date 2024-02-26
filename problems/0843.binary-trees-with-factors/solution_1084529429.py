# 0843 - Binary Trees With Factors
# Date: 2023-10-26
# Runtime: 444 ms, Memory: 17.8 MB
# Submission Id: 1084529429


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(arr)
        arr.sort()
        index = {num: idx for idx, num in enumerate(arr)}
        
        @cache
        def dp(i):
            res = 1
            for j in range(i):
                x, r = divmod(arr[i], arr[j])
                if r == 0 and x in index:
                    res = (res + dp(j) * dp(index[x])) % MOD
            return res
        
        ans = 0
        for i in range(n):
            ans += dp(i)
        return ans % MOD