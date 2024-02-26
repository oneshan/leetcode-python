# 0252 - Meeting Rooms
# Date: 2023-11-01
# Runtime: 91 ms, Memory: 20.4 MB
# Submission Id: 1089067398


import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        heap = []
        for start, end in intervals:
            heapq.heappush(heap, (start, 1))
            heapq.heappush(heap, (end, -1))
        
        curr = 0
        while heap:
            _, diff = heapq.heappop(heap)
            curr += diff
            if curr > 1:
                return False
        return True