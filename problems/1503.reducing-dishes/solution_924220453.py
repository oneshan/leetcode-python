# 1503 - Reducing Dishes
# Date: 2023-03-29
# Runtime: 39 ms, Memory: 13.9 MB
# Submission Id: 924220453


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        curr_sum = ans = 0
        for val in sorted(satisfaction, reverse=True):
            curr_sum += val
            if curr_sum <= 0:
                break
            ans += curr_sum
        return ans