# 2569 - Number of Beautiful Partitions
# Date: 2022-11-20
# Runtime: 8255 ms, Memory: 29.4 MB
# Submission Id: 846730208


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        primes = {'2', '3', '5', '7'}

        if k * minLength > n or s[0] not in primes or s[-1] in primes:
            return 0
        
        start_ids = [0]
        for i in range(1, n):
            if s[i] in primes and s[i-1] not in primes:
                start_ids.append(i)
        len_p = len(start_ids)
        
        @cache
        def dp(i, remains_k):
            if remains_k == 1:
                return 1 if start_ids[i]+minLength-1 <= n-1 else 0
            
            ans = 0
            for j in range(i+1, len_p-remains_k+2):
                if start_ids[j] - start_ids[i] >= minLength:
                    ans += dp(j, remains_k-1)
            return ans % (10**9 + 7)
        
        return dp(0, k)