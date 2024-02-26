# 0352 - Data Stream as Disjoint Intervals
# Date: 2023-01-28
# Runtime: 493 ms, Memory: 18.9 MB
# Submission Id: 886837311


class SummaryRanges:

    def __init__(self):
        self.nums = set()
        
    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        ans = []
        start = end = float('-inf')
        for curr in sorted(self.nums):
            if curr == end+1:
                end = curr
            else:
                ans.append([start, end])
                start = end = curr
        ans.append([start, end])
        return ans[1:]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()