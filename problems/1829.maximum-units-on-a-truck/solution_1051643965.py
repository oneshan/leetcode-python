# 1829 - Maximum Units on a Truck
# Date: 2023-09-17
# Runtime: 148 ms, Memory: 16.9 MB
# Submission Id: 1051643965


import heapq

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_heap = []
        for count, unit in boxTypes:
            heapq.heappush(max_heap, (-unit, count))
        
        ans = 0
        while max_heap and truckSize > 0:
            unit, count = heapq.heappop(max_heap)
            ans -= unit * min(count, truckSize)
            truckSize -= count
        return ans