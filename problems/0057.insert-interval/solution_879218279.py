# 0057 - Insert Interval
# Date: 2023-01-16
# Runtime: 86 ms, Memory: 17.2 MB
# Submission Id: 879218279


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx, n = 0, len(intervals)
        ans = []
        
        while idx < n and intervals[idx][1] < newInterval[0]:
            ans.append(intervals[idx])
            idx += 1
            
        while idx < n and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(intervals[idx][0], newInterval[0])
            newInterval[1] = max(intervals[idx][1], newInterval[1])
            idx += 1
        ans.append(newInterval)
        ans.extend(intervals[idx:])
        
        return ans