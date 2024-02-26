# 0056 - Merge Intervals
# Date: 2024-02-20
# Runtime: 129 ms, Memory: 21.3 MB
# Submission Id: 1180516118


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for start, end in intervals:
            if not ans or start > ans[-1][1]:
                ans.append([start, end])
            else:
                ans[-1][1] = max(ans[-1][1], end)
        return ans