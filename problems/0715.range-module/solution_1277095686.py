# 0715 - Range Module
# Date: 2024-06-04
# Runtime: 357 ms, Memory: 21.4 MB
# Submission Id: 1277095686


from sortedcontainers import SortedList

class RangeModule:

    def __init__(self):
        self.intervals = SortedList()

    def addRange(self, left: int, right: int) -> None:
        idx = self.intervals.bisect_left([left, right])
        while idx < len(self.intervals) and right >= self.intervals[idx][0]:
            right = max(right, self.intervals[idx][1])
            self.intervals.pop(idx)
        
        if idx and self.intervals[idx-1][1] >= left:
            self.intervals[idx-1][0] = min(left, self.intervals[idx-1][0])
            self.intervals[idx-1][1] = max(right, self.intervals[idx-1][1])
        else:
            self.intervals.add([left, right])

    def queryRange(self, left: int, right: int) -> bool:
        idx = self.intervals.bisect_left([left, right])
        if idx and self.intervals[idx-1][0] <= left < right <= self.intervals[idx-1][1]:
            return True
        if idx < len(self.intervals) and self.intervals[idx][0] <= left < right <= self.intervals[idx][1]:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        idx = self.intervals.bisect_left([left, right])
        while idx < len(self.intervals) and right >= self.intervals[idx][0]:
            if right < self.intervals[idx][1]:
                self.intervals[idx][0] = right
                break
            self.intervals.pop(idx)

        if idx and self.intervals[idx-1][1] > left:
            if self.intervals[idx-1][1] > right:
                self.intervals.add([right, self.intervals[idx-1][1]])
            self.intervals[idx-1][1] = left


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)