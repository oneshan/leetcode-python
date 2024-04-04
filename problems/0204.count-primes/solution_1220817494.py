# 0204 - Count Primes
# Date: 2024-04-02
# Runtime: 2233 ms, Memory: 55.2 MB
# Submission Id: 1220817494


class Solution:
    def countPrimes(self, n: int) -> int:
        not_prime = [False] * n
        
        ans = 0
        for i in range(2, n):
            if not_prime[i]:
                continue
            ans += 1
            for j in range(i+i, n, i):
                not_prime[j] = True

        return ans