# 1126 - Minimum Cost to Connect Sticks
# Date: 2022-11-01
# Runtime: 947 ms, Memory: 15.2 MB
# Submission Id: 834654667


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