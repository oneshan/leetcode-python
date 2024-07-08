# 2553 - Total Cost to Hire K Workers
# Date: 2024-06-16
# Runtime: 710 ms, Memory: 31 MB
# Submission Id: 1290179990


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        left, right = 0, len(costs)-1
        
        for i in range(candidates):
            if left <= right:
                heapq.heappush(heap, (costs[left], left))
                left += 1
            if left <= right:
                heapq.heappush(heap, (costs[right], right))
                right -= 1

        ans = 0
        for _ in range(k):
            cost, idx = heapq.heappop(heap)
            ans += cost
            if left <= right:
                if idx < left:
                    heapq.heappush(heap, (costs[left], left))
                    left += 1
                else:
                    heapq.heappush(heap, (costs[right], right))
                    right -= 1

        return ans