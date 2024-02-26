# 2553 - Total Cost to Hire K Workers
# Date: 2023-06-26
# Runtime: 914 ms, Memory: 28.6 MB
# Submission Id: 979771894


import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        
        heap = []
        for left in range(candidates):
            heap.append((costs[left], 0))
        for right in range(max(candidates, n - candidates), n):
            heap.append((costs[right], 1))
        heapq.heapify(heap)
        
        ans = 0
        left, right = candidates, n - candidates - 1
        for _ in range(k):
            cost, s_id = heapq.heappop(heap)
            ans += cost
            if left > right:
                continue
            if s_id == 0:
                heapq.heappush(heap, (costs[left], 0))
                left += 1
            else:
                heapq.heappush(heap, (costs[right], 1))
                right -= 1
        return ans