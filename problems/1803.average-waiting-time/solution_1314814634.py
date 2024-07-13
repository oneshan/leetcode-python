# 1803 - Average Waiting Time
# Date: 2024-07-09
# Runtime: 742 ms, Memory: 57.2 MB
# Submission Id: 1314814634


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        ans = curr = 0
        for arrival, time in customers:
            curr = max(arrival, curr) + time
            ans += (curr - arrival)

        return ans / len(customers)