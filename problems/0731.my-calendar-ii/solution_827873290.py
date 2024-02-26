# 0731 - My Calendar II
# Date: 2022-10-22
# Runtime: 5354 ms, Memory: 15.1 MB
# Submission Id: 827873290


from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.intervals = SortedDict()
        
    def book(self, start: int, end: int) -> bool:
        count = 0
        self.intervals[start] = self.intervals.get(start, 0) + 1
        self.intervals[end] = self.intervals.get(end, 0) - 1
        for ts, delta in self.intervals.items():
            if ts > end:
                break
            count += delta
            if count > 2:
                self.intervals[start] -= 1
                self.intervals[end] += 1
                return False
        return True
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)