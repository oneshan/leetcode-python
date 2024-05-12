# 0887 - Minimum Cost to Hire K Workers
# Date: 2024-05-11
# Runtime: 147 ms, Memory: 19 MB
# Submission Id: 1254979334


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # wage[j] = wage[i] * (quality[j] / quality[i])
        # Sum(wage) = (wage[i] / quality[i]) * Sum(quality)

        n = len(quality)
        ratios = [(wage[i] / quality[i], quality[i]) for i in range(n)]
        ratios.sort()

        max_heap = []
        ans = float('inf')
        curr = 0
        for ratio, quality in ratios:
            heapq.heappush(max_heap, -quality)
            curr += quality
            if len(max_heap) > k:
                curr += heapq.heappop(max_heap)
            if len(max_heap) == k:
                ans = min(ans, curr * ratio)

        return ans