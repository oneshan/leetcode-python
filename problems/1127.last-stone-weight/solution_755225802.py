# 1127 - Last Stone Weight
# Date: 2022-07-24
# Runtime: 95 ms, Memory: 13.8 MB
# Submission Id: 755225802


import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_weight = max(stones)  # O(N)
        buckets = [0] * (max_weight+1)
        
        for stone in stones:
            buckets[stone] += 1
            
        biggest = 0
        current = max_weight
        while current > 0:
            if buckets[current] == 0:
                current -= 1
            elif biggest == 0:
                buckets[current] &= 1
                if buckets[current]:
                    biggest = current
                current -= 1
            else:
                buckets[current] -= 1
                biggest -= current
                if biggest <= current:
                    buckets[biggest] += 1
                    biggest = 0
        return biggest