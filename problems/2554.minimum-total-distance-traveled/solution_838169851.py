# 2554 - Minimum Total Distance Traveled
# Date: 2022-11-07
# Runtime: 304 ms, Memory: 14.5 MB
# Submission Id: 838169851


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        len_r, len_f = len(robot), len(factory)
        
        dp = [[0] * (len_f+1) for _ in range(len_r+1)]
        for r_idx in range(len_r):
            dp[r_idx][-1] = float('inf')
            
        for f_idx in range(len_f-1, -1, -1):
            limit = factory[f_idx][1]
            prefix = 0
            heap = [(0, len_r)]
            for r_idx in range(len_r-1, -1, -1):
                while heap and heap[0][1] > r_idx + limit:
                    heapq.heappop(heap)
                prefix += abs(robot[r_idx] - factory[f_idx][0])
                heapq.heappush(heap, (dp[r_idx][f_idx+1] - prefix, r_idx))
                dp[r_idx][f_idx] = prefix + heap[0][0]
        return dp[0][0]