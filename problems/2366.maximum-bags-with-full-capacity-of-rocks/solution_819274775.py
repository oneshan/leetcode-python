# 2366 - Maximum Bags With Full Capacity of Rocks
# Date: 2022-10-10
# Runtime: 1039 ms, Memory: 22.1 MB
# Submission Id: 819274775


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remains = [capacity[i]-rocks[i] for i in range(len(rocks))]
        remains.sort()
        ans = 0
        for bags in remains:
            if additionalRocks < bags:
                break
            additionalRocks -= bags
            ans += 1
        return ans