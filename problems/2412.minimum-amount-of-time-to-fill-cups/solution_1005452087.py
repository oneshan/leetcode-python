# 2412 - Minimum Amount of Time to Fill Cups
# Date: 2023-07-27
# Runtime: 50 ms, Memory: 16.4 MB
# Submission Id: 1005452087


import heapq

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0
        pq = [-num for num in amount]
        heapq.heapify(pq)

        while pq[0]:
            ans += 1
            max1, max2 = heapq.heappop(pq), heapq.heappop(pq)
            heapq.heappush(pq, max1+1)
            heapq.heappush(pq, max2+1)
        
        return ans