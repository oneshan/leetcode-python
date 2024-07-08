# 1955 - Seat Reservation Manager
# Date: 2024-06-16
# Runtime: 398 ms, Memory: 51.3 MB
# Submission Id: 1290151729


class SeatManager:

    def __init__(self, n: int):
        self.reserved = set()
        self.free_seats = list(range(1, n+1))
        heapq.heapify(self.free_seats)

    def reserve(self) -> int:
        seat = heapq.heappop(self.free_seats)
        self.reserved.add(seat)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber not in self.reserved:
            return
        self.reserved.discard(seatNumber)
        heapq.heappush(self.free_seats, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)