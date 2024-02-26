# 2245 - Destroying Asteroids
# Date: 2022-10-10
# Runtime: 1175 ms, Memory: 27.8 MB
# Submission Id: 819171830


import heapq

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        heap = []
        for asteroid in asteroids:
            if asteroid > mass:
                heapq.heappush(heap, asteroid)
            else:
                mass += asteroid
        
        while heap:
            if heap[0] > mass:
                return False
            mass += heapq.heappop(heap)
        return True