# 1184 - Car Pooling
# Date: 2022-09-24
# Runtime: 144 ms, Memory: 14.4 MB
# Submission Id: 807362444


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ts = [0] * 1001
        for num_p, _from, _to in trips:
            ts[_from] += num_p
            ts[_to] -= num_p
            
        curr = 0
        for ps_change in ts:
            curr += ps_change
            if curr > capacity:
                return False
        return True