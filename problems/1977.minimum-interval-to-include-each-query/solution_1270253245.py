# 1977 - Minimum Interval to Include Each Query
# Date: 2024-05-28
# Runtime: 1292 ms, Memory: 58.1 MB
# Submission Id: 1270253245


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        i, n = 0, len(intervals)
        intervals.sort()
        heap = []  # (interval_length, end)

        table = {}
        for q in sorted(queries):

            while i < n and intervals[i][0] <= q:
                if intervals[i][1] >= q:
                    heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                table[q] = heap[0][0]
        

        return [table.get(q, -1) for q in queries]