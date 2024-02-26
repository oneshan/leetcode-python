# 1700 - Minimum Time to Make Rope Colorful
# Date: 2023-12-27
# Runtime: 834 ms, Memory: 28.3 MB
# Submission Id: 1129316194


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        curr_sum = curr_max = ans = 0
        for i in range(n):
            if i and colors[i] != colors[i-1]:
                ans += curr_sum - curr_max
                curr_sum = curr_max = 0

            curr_sum += neededTime[i]
            curr_max = max(curr_max, neededTime[i])

        ans += curr_sum - curr_max
        return ans