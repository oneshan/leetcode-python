# 1141 - How Many Apples Can You Put into the Basket
# Date: 2022-10-16
# Runtime: 241 ms, Memory: 14.1 MB
# Submission Id: 823538395


import heapq

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        heapq.heapify(weight)
        ans = total = 0
        while weight:
            total += heapq.heappop(weight)
            if total > 5000:
                break
            ans += 1
        return ans