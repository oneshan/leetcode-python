# 0732 - My Calendar III
# Date: 2022-10-22
# Runtime: 5100 ms, Memory: 14.8 MB
# Submission Id: 827876057


from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.intervals = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        ans = count = 0
        self.intervals[startTime] = self.intervals.get(startTime, 0) + 1
        self.intervals[endTime] = self.intervals.get(endTime, 0) - 1
        for ts, delta in self.intervals.items():
            count += delta
            ans = max(ans, count)
        return ans

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)