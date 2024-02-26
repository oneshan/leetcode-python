# 3192 - Maximum Xor Product
# Date: 2023-11-19
# Runtime: 39 ms, Memory: 16.3 MB
# Submission Id: 1101861758


class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 1000_000_007
        
        x = 0
        for i in range(n):
            mask = 1 << i
            if a & mask and b & mask:
                continue
            x ^= mask

        ans = (a ^ x) * (b ^ x)
        for i in range(n-1, -1, -1):
            mask = 1 << i
            if x & mask == 0:
                continue
            curr_mask = x ^ mask
            curr_prod = (a ^ curr_mask) * (b ^ curr_mask)
            if ans < curr_prod:
                x = curr_mask
                ans = curr_prod
        return ans % MOD