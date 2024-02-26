# 2366 - Maximum Bags With Full Capacity of Rocks
# Date: 2022-10-10
# Runtime: 2483 ms, Memory: 22 MB
# Submission Id: 819273266


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remains = [capacity[i]-rocks[i] for i in range(len(rocks))]
        remains.sort()
        ans = 0
        for bags in remains:
            additionalRocks -= bags
            if additionalRocks < 0:
                break
            ans += 1
        return ans