# 1503 - Reducing Dishes
# Date: 2023-03-29
# Runtime: 53 ms, Memory: 14 MB
# Submission Id: 924219786


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        curr_sum = ans = 0
        for val in sorted(satisfaction, reverse=True):
            if curr_sum + val <= 0:
                break
            curr_sum += val
            ans += curr_sum
        return ans