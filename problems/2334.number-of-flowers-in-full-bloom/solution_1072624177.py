# 2334 - Number of Flowers in Full Bloom
# Date: 2023-10-11
# Runtime: 933 ms, Memory: 43.6 MB
# Submission Id: 1072624177


import heapq

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        heap = []
        flowers.sort()
        seen = {}
        
        i, n = 0, len(flowers)
        for person in sorted(set(people)):
            while i < n and person >= flowers[i][0]:
                heapq.heappush(heap, flowers[i][1])
                i += 1
            
            while heap and heap[0] < person:
                heapq.heappop(heap)
            
            seen[person] = len(heap)
        
        return [seen[person] for person in people]