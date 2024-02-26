# 0253 - Meeting Rooms II
# Date: 2022-10-09
# Runtime: 116 ms, Memory: 17.9 MB
# Submission Id: 818213686


import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        for start, end in intervals:
            heapq.heappush(heap, (start, 1))
            heapq.heappush(heap, (end, -1))
        
        ans = curr = 0
        while heap:
            ts, delta = heapq.heappop(heap)
            print(ts, delta)
            curr += delta
            ans = max(ans, curr)
        return ans