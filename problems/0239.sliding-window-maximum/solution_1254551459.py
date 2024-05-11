# 0239 - Sliding Window Maximum
# Date: 2024-05-10
# Runtime: 1332 ms, Memory: 42 MB
# Submission Id: 1254551459


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        max_heap = []
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        
        ans = [-max_heap[0][0]]
        for i in range(k, n):
            heapq.heappush(max_heap, (-nums[i], i))
            while max_heap[0][-1] <= i - k:
                heapq.heappop(max_heap)
            ans.append(-max_heap[0][0])
        return ans