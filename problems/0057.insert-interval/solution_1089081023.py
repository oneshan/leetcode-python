# 0057 - Insert Interval
# Date: 2023-11-01
# Runtime: 82 ms, Memory: 19.9 MB
# Submission Id: 1089081023


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx, n = 0, len(intervals)
        ans = []
        
        while idx < n and intervals[idx][1] < newInterval[0]:
            ans.append(intervals[idx])
            idx += 1
        
        ans.append(newInterval)
        while idx < n and min(ans[-1][1], intervals[idx][1]) >= max(ans[-1][0], intervals[idx][0]):
            ans[-1] = (min(ans[-1][0], intervals[idx][0]), max(ans[-1][1], intervals[idx][1]))
            idx += 1
            
        ans += intervals[idx:]
        return ans