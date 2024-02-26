# 0252 - Meeting Rooms
# Date: 2023-11-01
# Runtime: 75 ms, Memory: 19.5 MB
# Submission Id: 1089058876


import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        prev_end = -1
        for start, end in intervals:
            if prev_end > start:
                return False
            prev_end = end
        return True