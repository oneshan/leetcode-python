# 1063 - Best Sightseeing Pair
# Date: 2022-10-27
# Runtime: 512 ms, Memory: 20.6 MB
# Submission Id: 831080105


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans, curr = 0, values[0]
        for i in range(1, len(values)):
            ans = max(ans, curr + values[i] - i)
            curr = max(curr, values[i] + i)
        return ans