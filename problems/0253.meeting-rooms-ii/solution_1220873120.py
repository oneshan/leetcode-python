# 0253 - Meeting Rooms II
# Date: 2024-04-02
# Runtime: 67 ms, Memory: 19.9 MB
# Submission Id: 1220873120


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        intervals.sort()

        ans = 0
        for start, end in intervals:
            while rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
            ans = max(ans, len(rooms))
        return ans