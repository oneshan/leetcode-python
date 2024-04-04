# 0253 - Meeting Rooms II
# Date: 2024-04-02
# Runtime: 77 ms, Memory: 20.4 MB
# Submission Id: 1220869915


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        times = []
        for start, end in intervals:
            times.append((start, 1))
            times.append((end, -1))
        
        times.sort()
        ans = count = 0
        for _, delta in times:
            count += delta
            ans = max(ans, count)
        return ans