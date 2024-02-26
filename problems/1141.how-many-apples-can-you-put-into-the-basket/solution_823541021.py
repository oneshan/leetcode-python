# 1141 - How Many Apples Can You Put into the Basket
# Date: 2022-10-16
# Runtime: 195 ms, Memory: 14.1 MB
# Submission Id: 823541021


import heapq

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        bucket = [0] * 1001
        for w in weight:
            bucket[w] += 1
        
        ans = total = 0
        for i in range(1001):
            if bucket[i] == 0:
                continue
                
            take = min(bucket[i], (5000-total) // i)
            if take == 0:
                break
            ans += take
            total += take * i
        return ans