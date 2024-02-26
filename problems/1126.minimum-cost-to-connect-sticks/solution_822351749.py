# 1126 - Minimum Cost to Connect Sticks
# Date: 2022-10-14
# Runtime: 394 ms, Memory: 15 MB
# Submission Id: 822351749


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