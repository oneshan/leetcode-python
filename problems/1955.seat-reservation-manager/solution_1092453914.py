# 1955 - Seat Reservation Manager
# Date: 2023-11-06
# Runtime: 372 ms, Memory: 42.4 MB
# Submission Id: 1092453914


import heapq

class SeatManager:

    def __init__(self, n: int):
        self.marker = 1
        self.available_seats = []

    def reserve(self) -> int:
        if self.available_seats:
            return heapq.heappop(self.available_seats)
        
        self.marker += 1
        return self.marker - 1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available_seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)