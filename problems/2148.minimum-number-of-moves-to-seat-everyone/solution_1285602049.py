# 2148 - Minimum Number of Moves to Seat Everyone
# Date: 2024-06-12
# Runtime: 62 ms, Memory: 16.5 MB
# Submission Id: 1285602049


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        ans = 0
        for seat, student in zip(seats, students):
            ans += abs(seat - student)
        return ans