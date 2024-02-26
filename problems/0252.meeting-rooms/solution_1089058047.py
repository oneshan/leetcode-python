# 0252 - Meeting Rooms
# Date: 2023-11-01
# Runtime: 80 ms, Memory: 19.6 MB
# Submission Id: 1089058047


import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        heapq.heapify(intervals)
        
        prev_end = 0
        while intervals:
            start, end = heapq.heappop(intervals)
            if prev_end > start:
                return False
            prev_end = end
        return True