# 0843 - Binary Trees With Factors
# Date: 2023-10-26
# Runtime: 483 ms, Memory: 16.3 MB
# Submission Id: 1084528031


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(arr)
        arr.sort()
        
        dp = [1] * n
        index = {num: idx for idx, num in enumerate(arr)}
        for i in range(n):
            for j in range(i):
                x, r = divmod(arr[i], arr[j])
                if r == 0 and x in index:
                    dp[i] = (dp[i] + dp[j] * dp[index[x]]) % MOD
        return sum(dp) % MOD