# 0253 - Meeting Rooms II
# Date: 2022-10-09
# Runtime: 80 ms, Memory: 17.7 MB
# Submission Id: 818216994


import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        checking = []
        for start, end in intervals:
            checking.append((start, 1))
            checking.append((end, -1))
        checking.sort()
        
        ans = curr = 0
        for ts, delta in checking:
            curr += delta
            ans = max(ans, curr)
        return ans