# 0629 - K Inverse Pairs Array
# Date: 2024-01-27
# Runtime: 1167 ms, Memory: 433.7 MB
# Submission Id: 1157992078


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        
        MOD = 1_000_000_007
        
        @cache
        def pairs(n: int, k: int) -> int:
            max_pairs = (n * (n - 1)) // 2
            # no inverse pair possible
            if n == 0 or k < 0 or k > max_pairs:
                return 0
            # exactly one inverse pair possible
            if k == 0 or k == max_pairs:
                return 1
            return (pairs(n - 1, k) + pairs(n, k - 1) - pairs(n - 1, k - n)) % MOD

        return pairs(n, k)