# 1583 - Paint House III
# Date: 2024-05-06
# Runtime: 1160 ms, Memory: 17.4 MB
# Submission Id: 1250994893


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        dp = {(0, 0): 0}
        for i in range(m):
            new_dp = {}
            for c in (range(1, n+1) if houses[i] == 0 else [houses[i]]):
                for (prev_c, prev_t), prev_cost in dp.items():
                    next_t = prev_t if c == prev_c else prev_t + 1
                    next_cost = prev_cost + (cost[i][c-1] if houses[i] == 0 else 0)
                    if next_t > target:
                        continue
                    if (c, next_t) not in new_dp:
                        new_dp[(c, next_t)] = next_cost
                    else:
                        new_dp[(c, next_t)] = min(new_dp[(c, next_t)], next_cost)
            dp = new_dp
        
        return min([dp[(c, t)] for c, t in dp if t == target] or [-1])