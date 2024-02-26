# 0252 - Meeting Rooms
# Date: 2022-10-09
# Runtime: 80 ms, Memory: 17.4 MB
# Submission Id: 817984203


import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        heapq.heapify(intervals)  # O(N)
        
        prev_end = 0
        while intervals: # O(N)
            start, end = heapq.heappop(intervals) # O(logN)
            if start < prev_end:
                return False
            prev_end = end
        return True