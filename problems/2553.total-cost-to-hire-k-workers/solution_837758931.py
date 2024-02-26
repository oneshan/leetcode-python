# 2553 - Total Cost to Hire K Workers
# Date: 2022-11-06
# Runtime: 841 ms, Memory: 24.6 MB
# Submission Id: 837758931


import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if k >= len(costs):
            return sum(costs)
        
        min_heap_left = []
        min_heap_right = []
        
        left, right = 0, len(costs)-1
        for _ in range(candidates):
            heapq.heappush(min_heap_left, costs[left])
            left += 1
        for _ in range(candidates):
            if right >= left:
                heapq.heappush(min_heap_right, costs[right])
                right -= 1
                
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