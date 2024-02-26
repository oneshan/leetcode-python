# 2251 - Number of Ways to Divide a Long Corridor
# Date: 2023-11-28
# Runtime: 374 ms, Memory: 17.4 MB
# Submission Id: 1107807944


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007
        n = len(corridor)
        
        ans, seats, prev_idx = 1, 0, None
        for idx in range(n):
            if corridor[idx] == 'P':
                continue
            seats += 1
            if seats == 2:
                prev_idx = idx
                seats = 0
            elif seats == 1 and prev_idx is not None:
                ans = ans * (idx - prev_idx) % MOD

        if seats == 1 or prev_idx is None:
            return 0
        
        return ans