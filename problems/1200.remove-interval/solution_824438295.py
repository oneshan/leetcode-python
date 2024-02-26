# 1200 - Remove Interval
# Date: 2022-10-17
# Runtime: 402 ms, Memory: 21.7 MB
# Submission Id: 824438295


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        
        for start, end in intervals:
            if end < toBeRemoved[0] or start > toBeRemoved[1]:
                ans.append([start, end])
            else:
                if start < toBeRemoved[0]:
                    ans.append([start, toBeRemoved[0]])
                if end > toBeRemoved[1]:
                    ans.append([toBeRemoved[1], end])
        return ans