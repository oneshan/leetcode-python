# 0729 - My Calendar I
# Date: 2022-10-22
# Runtime: 571 ms, Memory: 14.9 MB
# Submission Id: 827860753


class MyCalendar:

    def __init__(self):
        self.intervals = []
        

    def book(self, start: int, end: int) -> bool:
        if not self.intervals:
            self.intervals.append([start, end])
            return True
        left, right = 0, len(self.intervals)-1
        while left <= right:
            mid = (left + right) // 2
            if self.intervals[mid][1] <= start:
                left = mid + 1
            elif self.intervals[mid][0] >= end:
                right = mid - 1
            else:
                return False
                
        self.intervals.insert(left, [start, end])
        return True
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)