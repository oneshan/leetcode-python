# 1955 - Seat Reservation Manager
# Date: 2023-11-06
# Runtime: 424 ms, Memory: 44 MB
# Submission Id: 1092452433


import heapq

class SeatManager:

    def __init__(self, n: int):
        self.arr = list(range(1, n+1))
        heapq.heapify(self.arr)

    def reserve(self) -> int:
        return heapq.heappop(self.arr)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.arr, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)