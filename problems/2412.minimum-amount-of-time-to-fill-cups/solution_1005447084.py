# 2412 - Minimum Amount of Time to Fill Cups
# Date: 2023-07-27
# Runtime: 40 ms, Memory: 16.2 MB
# Submission Id: 1005447084


import heapq

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0
        pq = [-num for num in amount if num]
        heapq.heapify(pq)

        while len(pq) > 1:
            ans += 1
            max1, max2 = heapq.heappop(pq), heapq.heappop(pq)
            if max1 < -1:
                heapq.heappush(pq, max1+1)
            if max2 < - 1:
                heapq.heappush(pq, max2+1)
        
        return ans - pq[0] if pq else ans