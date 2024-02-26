# 1700 - Minimum Time to Make Rope Colorful
# Date: 2023-12-27
# Runtime: 900 ms, Memory: 28.4 MB
# Submission Id: 1129317640


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        curr_max = ans = 0
        for i in range(n):
            if i and colors[i] != colors[i-1]:
                curr_max = 0
            
            ans += min(curr_max, neededTime[i])
            curr_max = max(curr_max, neededTime[i])

        return ans