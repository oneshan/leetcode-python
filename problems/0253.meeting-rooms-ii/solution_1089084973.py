# 0253 - Meeting Rooms II
# Date: 2023-11-01
# Runtime: 95 ms, Memory: 20.6 MB
# Submission Id: 1089084973


import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        heap = []
        for start, end in intervals:
            heapq.heappush(heap, (start, 1))
            heapq.heappush(heap, (end, -1))
            
        ans = curr = 0
        while heap:
            _, diff = heapq.heappop(heap)
            curr += diff
            ans = max(ans, curr)
        return ans