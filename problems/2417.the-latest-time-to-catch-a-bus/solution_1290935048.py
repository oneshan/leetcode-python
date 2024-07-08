# 2417 - The Latest Time to Catch a Bus
# Date: 2024-06-17
# Runtime: 533 ms, Memory: 36.1 MB
# Submission Id: 1290935048


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        i, n = 0, len(passengers)
        for bus in buses:
            curr_capacity = capacity
            while curr_capacity and i < n and passengers[i] <= bus:
                i += 1
                curr_capacity -= 1
        
        ans = bus if curr_capacity else passengers[i-1]
        used_time = set(passengers)
        while ans in used_time:
            ans -= 1

        return ans