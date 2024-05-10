# 3351 - Maximize Happiness of Selected Children
# Date: 2024-05-09
# Runtime: 823 ms, Memory: 43.4 MB
# Submission Id: 1253133519


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_heap = []
        ans = 0

        # O(N logN)
        for num in happiness:
            heapq.heappush(max_heap, -num)

        # O(k logN)
        for i in range(k):
            val = -heapq.heappop(max_heap) - i
            if val < 0:
                break
            ans += val

        return ans