# 0253 - Meeting Rooms II
# Date: 2022-11-01
# Runtime: 175 ms, Memory: 17.6 MB
# Submission Id: 834663574


import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort()
        free_rooms = []
        for start, end in intervals:
            if free_rooms and free_rooms[0] <= start:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, end)
        return len(free_rooms)