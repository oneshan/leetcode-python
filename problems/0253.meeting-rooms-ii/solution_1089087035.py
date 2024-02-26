# 0253 - Meeting Rooms II
# Date: 2023-11-01
# Runtime: 65 ms, Memory: 19.7 MB
# Submission Id: 1089087035


import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort()
        rooms = []
        ans = 0
        for start, end in intervals:
            while rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
            ans = max(ans, len(rooms))
        return ans