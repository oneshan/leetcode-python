# 2417 - The Latest Time to Catch a Bus
# Date: 2023-09-22
# Runtime: 609 ms, Memory: 35.9 MB
# Submission Id: 1056353009


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        buses.sort()
        n = len(passengers)
        
        i = 0
        for bus in buses:
            curr_capacity = capacity
            while curr_capacity and i < n and passengers[i] <= bus:
                curr_capacity -= 1
                i += 1
        ans = bus if curr_capacity else passengers[i-1]
        
        passengers = set(passengers)
        while ans in passengers:
            ans -= 1
        return ans