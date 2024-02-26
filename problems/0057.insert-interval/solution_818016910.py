# 0057 - Insert Interval
# Date: 2022-10-09
# Runtime: 91 ms, Memory: 17.4 MB
# Submission Id: 818016910


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx, n = 0, len(intervals)
        
        ans = []
        # append non-overlapping intervals
        while idx < n and intervals[idx][1] < newInterval[0]:
            ans.append(intervals[idx])
            idx += 1
        
        # merge overlapping intervals
        while idx < n and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
        ans.append(newInterval)
         
        # append remaining intervals
        while idx < n:
            ans.append(intervals[idx])
            idx += 1

        return ans