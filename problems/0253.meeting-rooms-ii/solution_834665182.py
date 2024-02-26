# 0253 - Meeting Rooms II
# Date: 2022-11-01
# Runtime: 189 ms, Memory: 17.5 MB
# Submission Id: 834665182


import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        rooms = []
        for start, end in sorted(intervals):
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        return len(rooms)