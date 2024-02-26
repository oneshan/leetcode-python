# 1063 - Best Sightseeing Pair
# Date: 2022-10-27
# Runtime: 492 ms, Memory: 20.7 MB
# Submission Id: 831077540


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        ans, curr_j = 0, values[-1] - (n-1)
        for i in range(len(values)-2, -1, -1):
            ans = max(ans, values[i]+i+curr_j)
            curr_j = max(curr_j, values[i]-i)
        return ans