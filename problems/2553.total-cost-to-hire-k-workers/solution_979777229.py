# 2553 - Total Cost to Hire K Workers
# Date: 2023-06-26
# Runtime: 823 ms, Memory: 27 MB
# Submission Id: 979777229


import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        
        min_heap_left, min_heap_right = [], []
        for left in range(candidates):
            heapq.heappush(min_heap_left, costs[left])
        for right in range(max(candidates, n-candidates), n):
            heapq.heappush(min_heap_right, costs[right])
            
        left, right = candidates, n-1-candidates
        ans = 0
        for _ in range(k):
            if not min_heap_left:
                ans += heapq.heappop(min_heap_right)
                continue
            if not min_heap_right:
                ans += heapq.heappop(min_heap_left)
                continue
                
            if min_heap_left[0] <= min_heap_right[0]:
                ans += heapq.heappop(min_heap_left)
                if left <= right:
                    heapq.heappush(min_heap_left, costs[left])
                    left += 1
            else:
                ans += heapq.heappop(min_heap_right)
                if left <= right:
                    heapq.heappush(min_heap_right, costs[right])
                    right -= 1
        return ans