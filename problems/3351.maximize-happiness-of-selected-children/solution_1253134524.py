# 3351 - Maximize Happiness of Selected Children
# Date: 2024-05-09
# Runtime: 835 ms, Memory: 43.5 MB
# Submission Id: 1253134524


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0

        # O(N)
        max_heap = [-h for h in happiness]
        heapq.heapify(max_heap)

        # O(k logN)
        for i in range(k):
            val = -heapq.heappop(max_heap) - i
            if val < 0:
                break
            ans += val

        return ans