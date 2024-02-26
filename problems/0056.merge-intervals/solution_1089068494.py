# 0056 - Merge Intervals
# Date: 2023-11-01
# Runtime: 139 ms, Memory: 21.2 MB
# Submission Id: 1089068494


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        ans = []
        for start, end in intervals:
            if not ans or ans[-1][1] < start:
                ans.append([start, end])
            else:
                ans[-1][1] = max(ans[-1][1], end)
        return ans