# 1616 - Minimum Difference Between Largest and Smallest Value in Three Moves
# Date: 2024-07-03
# Runtime: 306 ms, Memory: 27.6 MB
# Submission Id: 1307863855


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0

        min_heap = [] # largest 4
        max_heap = [] # smallest 4

        for idx, num in enumerate(nums):
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if idx > 3:
                heapq.heappop(min_heap)
                heapq.heappop(max_heap)
        
        small_4 = []  # reverse order
        large_4 = []
        for i in range(4):
            large_4.append(heapq.heappop(min_heap))
            small_4.append(-heapq.heappop(max_heap))

        ans = float('inf')
        for i in range(4):
            ans = min(ans, large_4[i] - small_4[~i])
        
        return ans