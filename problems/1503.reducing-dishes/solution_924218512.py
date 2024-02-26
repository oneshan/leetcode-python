# 1503 - Reducing Dishes
# Date: 2023-03-29
# Runtime: 48 ms, Memory: 13.8 MB
# Submission Id: 924218512


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        curr_sum = ans = 0
        for idx, val in enumerate(satisfaction):
            if curr_sum + val <= 0:
                break
            curr_sum += val
            ans += curr_sum
        return ans