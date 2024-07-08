# 0252 - Meeting Rooms
# Date: 2024-05-28
# Runtime: 72 ms, Memory: 19.9 MB
# Submission Id: 1270228099


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        prev_end = float('-inf')
        for start, end in intervals:
            if start < prev_end:
                return False
            prev_end = max(prev_end, end)
        return True