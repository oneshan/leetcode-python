# 2251 - Number of Ways to Divide a Long Corridor
# Date: 2023-11-28
# Runtime: 3790 ms, Memory: 137.1 MB
# Submission Id: 1107801055


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007
        n = len(corridor)
        
        cache = [[-1] * 3 for i in range(n)]
        
        def count(index, seats):
            if index == n:
                return 1 if seats == 2 else 0
            
            if cache[index][seats] != -1:
                return cache[index][seats]
            
            if corridor[index] == 'S':
                res = count(index+1, 1 if seats == 2 else seats + 1)
            else:
                if seats == 2:
                    res = (count(index+1, seats) + count(index+1, 0)) % MOD
                else:
                    res = count(index+1, seats)
            
            cache[index][seats] = res
            return res
        
        return count(0, 0) % MOD