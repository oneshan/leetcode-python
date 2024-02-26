# 2049 - Eliminate Maximum Number of Monsters
# Date: 2023-11-07
# Runtime: 672 ms, Memory: 32.1 MB
# Submission Id: 1093544895


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrive_time = [d / s for d, s in zip(dist, speed)]
        arrive_time.sort()
        
        n = len(arrive_time)
        for i in range(n):
            if arrive_time[i] <= i:
                return i
        return n