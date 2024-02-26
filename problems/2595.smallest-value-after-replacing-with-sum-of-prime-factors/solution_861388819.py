# 2595 - Smallest Value After Replacing With Sum of Prime Factors
# Date: 2022-12-18
# Runtime: 54 ms, Memory: 13.9 MB
# Submission Id: 861388819


class Solution:
    def smallestValue(self, n: int) -> int:
        def sum_prime_factors(num):
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    return i + sum_prime_factors(num//i)
            return num
        
        ans = n
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum_prime_factors(n)
            ans = min(ans, n)
        return ans