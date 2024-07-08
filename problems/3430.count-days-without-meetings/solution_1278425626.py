# 3430 - Count Days Without Meetings
# Date: 2024-06-05
# Runtime: 1418 ms, Memory: 66.7 MB
# Submission Id: 1278425626


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ans = prev_end = 0
        for start, end in meetings:
            if start > prev_end:
                ans += (start - prev_end - 1)
            prev_end = max(prev_end, end)
        ans += days - prev_end
        return ans