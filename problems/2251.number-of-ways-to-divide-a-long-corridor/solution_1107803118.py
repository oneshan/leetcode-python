# 2251 - Number of Ways to Divide a Long Corridor
# Date: 2023-11-28
# Runtime: 558 ms, Memory: 17.4 MB
# Submission Id: 1107803118


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007
        n = len(corridor)
        
        count = [0, 0, 1]
        
        for i in range(n-1, -1, -1):
            if corridor[i] == 'S':
                count[0], count[1], count[2] = count[1], count[2], count[1]
            else:
                count[2] = (count[0] + count[2]) % MOD
        
        return count[0]