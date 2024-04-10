# 2195 - Time Needed to Buy Tickets
# Date: 2024-04-09
# Runtime: 42 ms, Memory: 16.5 MB
# Submission Id: 1227235275


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i in range(k+1):
            ans += min(tickets[k], tickets[i])
        for i in range(k+1, len(tickets)):
            ans += min(tickets[k]-1, tickets[i])
        return ans