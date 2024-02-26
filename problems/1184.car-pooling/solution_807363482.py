# 1184 - Car Pooling
# Date: 2022-09-24
# Runtime: 179 ms, Memory: 14.5 MB
# Submission Id: 807363482


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ts = []
        for num_p, _from, _to in trips:
            ts.append((_from, num_p))
            ts.append((_to, -num_p))
        
        ts.sort()

        curr = 0
        for _, ps_change in ts:
            curr += ps_change
            if curr > capacity:
                return False
        return True