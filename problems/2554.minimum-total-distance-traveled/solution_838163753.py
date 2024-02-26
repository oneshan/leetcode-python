# 2554 - Minimum Total Distance Traveled
# Date: 2022-11-07
# Runtime: 7779 ms, Memory: 459.6 MB
# Submission Id: 838163753


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        len_r = len(robot)
        len_f = len(factory)
        
        @lru_cache(None)
        def recur(r_idx, f_idx, f_limit):
            if r_idx >= len_r:
                return 0
            if f_idx >= len_f:
                return float('inf')
            if f_limit <= 0:
                if f_idx + 1 < len_f:
                    return recur(r_idx, f_idx+1, factory[f_idx+1][1])
                return float('inf')
            dist = abs(robot[r_idx] - factory[f_idx][0])
            take = dist + recur(r_idx+1, f_idx, f_limit-1)
            non_take = recur(r_idx, f_idx, -1)
            return min(take, non_take)
        
        return recur(0, 0, factory[0][1])