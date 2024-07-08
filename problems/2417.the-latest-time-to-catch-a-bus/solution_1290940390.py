# 2417 - The Latest Time to Catch a Bus
# Date: 2024-06-17
# Runtime: 525 ms, Memory: 35 MB
# Submission Id: 1290940390


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        i, n = 0, len(passengers)
        ans = c = 0
        for bus in buses:
            while c < capacity and i < n and passengers[i] <= bus:
                if i == 0 or passengers[i] - 1 != passengers[i-1]:
                    ans = passengers[i] - 1
                i += 1
                c += 1
            
            if c < capacity and (i == 0 or passengers[i-1] < bus):
                ans = bus
            c = 0

        return ans