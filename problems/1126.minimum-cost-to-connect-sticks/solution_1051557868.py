# 1126 - Minimum Cost to Connect Sticks
# Date: 2023-09-17
# Runtime: 279 ms, Memory: 17.4 MB
# Submission Id: 1051557868


import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        ans = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            s1 = heapq.heappop(sticks)
            s2 = heapq.heappop(sticks)
            ans += (s1+s2)
            heapq.heappush(sticks, s1+s2)
        return ans