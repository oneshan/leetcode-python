# 2251 - Number of Ways to Divide a Long Corridor
# Date: 2023-11-28
# Runtime: 345 ms, Memory: 21.3 MB
# Submission Id: 1107806099


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007
        n = len(corridor)
        
        arr = [idx for idx in range(n) if corridor[idx] == 'S']
        m = len(arr)
        if m & 1 or len(arr) < 2:
            return 0
        
        ans = 1
        for i in range(1, m-1, 2):
            ans = ans * (arr[i+1] - arr[i]) % MOD
        return ans