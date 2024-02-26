# 1184 - Car Pooling
# Date: 2022-09-24
# Runtime: 186 ms, Memory: 14.4 MB
# Submission Id: 807360449


import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ts = []
        for num_p, _from, _to in trips:
            heapq.heappush(ts, (_from, num_p))
            heapq.heappush(ts, (_to, -num_p))
        
        curr = 0
        while ts:
            _, num_p = heapq.heappop(ts)
            curr += num_p
            if curr > capacity:
                return False
        return True