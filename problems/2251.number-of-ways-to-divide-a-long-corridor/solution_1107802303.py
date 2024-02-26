# 2251 - Number of Ways to Divide a Long Corridor
# Date: 2023-11-28
# Runtime: 1955 ms, Memory: 30.6 MB
# Submission Id: 1107802303


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007
        n = len(corridor)
        
        count = [[-1] * 3 for i in range(n+1)]
        count[-1][0], count[-1][1], count[-1][2] = 0, 0, 1
        
        for i in range(n-1, -1, -1):
            if corridor[i] == 'S':
                count[i][0] = count[i+1][1]
                count[i][1] = count[i+1][2]
                count[i][2] = count[i+1][1]
            else:
                count[i][0] = count[i+1][0]
                count[i][1] = count[i+1][1]
                count[i][2] = (count[i+1][0] + count[i+1][2]) % MOD
        
        return count[0][0]