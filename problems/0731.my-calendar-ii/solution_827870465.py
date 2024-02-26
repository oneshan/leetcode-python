# 0731 - My Calendar II
# Date: 2022-10-22
# Runtime: 1026 ms, Memory: 14.7 MB
# Submission Id: 827870465


class MyCalendarTwo:

    def __init__(self):
        self.intervals = []
        self.overlaps = []
        
    def book(self, start: int, end: int) -> bool:
        for p_start, p_end in self.overlaps:
            if not (start >= p_end or end <= p_start):
                return False
        for p_start, p_end in self.intervals:
            if not (start >= p_end or end <= p_start):
                self.overlaps.append((max(start, p_start), min(end, p_end)))
        self.intervals.append((start, end))
        return True
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)