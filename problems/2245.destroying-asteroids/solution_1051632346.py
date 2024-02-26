# 2245 - Destroying Asteroids
# Date: 2023-09-17
# Runtime: 1095 ms, Memory: 27.6 MB
# Submission Id: 1051632346


import heapq

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        heapq.heapify(asteroids)
        while asteroids and asteroids[0] <= mass:
            mass += heapq.heappop(asteroids)
        return len(asteroids) == 0