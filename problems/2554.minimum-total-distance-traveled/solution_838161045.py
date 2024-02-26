# 2554 - Minimum Total Distance Traveled
# Date: 2022-11-07
# Runtime: 4875 ms, Memory: 426.3 MB
# Submission Id: 838161045


import heapq

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        len_r = len(robot)
        len_f = len(factory)
        
        m, n = len(robot), len(factory)
        
        memo = {}
        
        def recur(r_idx, f_idx, f_limit):
            if r_idx >= len_r:
                return 0
            if f_idx >= len_f:
                return float('inf')
            if f_limit <= 0:
                if f_idx + 1 < len_f:
                    return recur(r_idx, f_idx+1, factory[f_idx+1][1])
                return float('inf')
            if (r_idx, f_idx, f_limit) not in memo:
                dist = abs(robot[r_idx] - factory[f_idx][0])
                take = dist + recur(r_idx+1, f_idx, f_limit-1)
                non_take = recur(r_idx, f_idx, -1)
                memo[(r_idx, f_idx, f_limit)] = min(take, non_take)
            return memo[(r_idx, f_idx, f_limit)]
        
        return recur(0, 0, factory[0][1])