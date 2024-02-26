# 0056 - Merge Intervals
# Date: 2022-10-09
# Runtime: 281 ms, Memory: 18.8 MB
# Submission Id: 817987868


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        ans = []
        for start, end in intervals:
            if ans and ans[-1][1] >= start:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start,end])
        return ans