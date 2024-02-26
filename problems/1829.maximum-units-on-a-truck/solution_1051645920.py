# 1829 - Maximum Units on a Truck
# Date: 2023-09-17
# Runtime: 151 ms, Memory: 16.7 MB
# Submission Id: 1051645920


import heapq

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        
        ans = 0
        for count, unit in boxTypes:
            if truckSize <= 0:
                break
            ans += unit * min(count, truckSize)
            truckSize -= count
        return ans