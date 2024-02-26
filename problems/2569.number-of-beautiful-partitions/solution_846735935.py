# 2569 - Number of Beautiful Partitions
# Date: 2022-11-20
# Runtime: 648 ms, Memory: 14 MB
# Submission Id: 846735935


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        primes = {'2', '3', '5', '7'}

        if k * minLength > n or s[0] not in primes or s[-1] in primes:
            return 0
        
        start_ids = {i for i in range(n-1) if s[i] not in primes and s[i+1] in primes}
        
        dp = [1] * (n-minLength)
        mod = 10 ** 9 + 7
        for j in range(1, k):
            new_dp = [0] * (n-minLength)
            for i in range(j*minLength-1, n-minLength):
                new_dp[i] = new_dp[i-1]
                if i in start_ids:
                    new_dp[i] += dp[i-minLength]
                new_dp[i] %= mod
            dp = new_dp
        return dp[-1]