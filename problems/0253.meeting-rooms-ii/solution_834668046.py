# 0253 - Meeting Rooms II
# Date: 2022-11-01
# Runtime: 231 ms, Memory: 17.5 MB
# Submission Id: 834668046


import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        ans = 0
        rooms = []
        for start, end in sorted(intervals):
            while rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
            ans = max(ans, len(rooms))
        return ans