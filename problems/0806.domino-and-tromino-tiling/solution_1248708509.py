# 0806 - Domino and Tromino Tiling
# Date: 2024-05-04
# Runtime: 44 ms, Memory: 16.6 MB
# Submission Id: 1248708509


class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        
        MOD = 1_000_000_007
        
        full = [0] * (n+1)
        part = [0] * (n+1)
        
        full[1] = 1
        full[2] = 2
        part[2] = 2
        
        for i in range(3, n+1):
            full[i] = (full[i-1] + full[i-2] + part[i-1]) % MOD
            part[i] = (2 * full[i-2] + part[i-1]) % MOD
        return full[-1]