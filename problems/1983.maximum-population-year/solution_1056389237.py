# 1983 - Maximum Population Year
# Date: 2023-09-22
# Runtime: 54 ms, Memory: 16.3 MB
# Submission Id: 1056389237


import heapq

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        heap = []
        for birth, death in logs:
            heapq.heappush(heap, (birth, 1))
            heapq.heappush(heap,(death, -1))
        
        ans = max_count = count = 0
        while heap:
            year, delta = heapq.heappop(heap)
            count += delta
            while heap and heap[0][0] == year:
                _, delta = heapq.heappop(heap)
                count += delta
            if count > max_count:
                ans = year
                max_count = count
        return ans