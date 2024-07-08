# 2148 - Minimum Number of Moves to Seat Everyone
# Date: 2024-06-13
# Runtime: 60 ms, Memory: 16.5 MB
# Submission Id: 1286736440


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        buckets = [0] * (1 + max(max(seats), max(students)))

        for s in seats:
            buckets[s] += 1
        
        for s in students:
            buckets[s] -= 1

        ans = curr = 0
        for diff in buckets:
            ans += abs(curr)
            curr += diff
        return ans