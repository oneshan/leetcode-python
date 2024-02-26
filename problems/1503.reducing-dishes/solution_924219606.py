# 1503 - Reducing Dishes
# Date: 2023-03-29
# Runtime: 45 ms, Memory: 14 MB
# Submission Id: 924219606


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        curr_sum = ans = 0
        for val in satisfaction:
            if curr_sum + val <= 0:
                break
            curr_sum += val
            ans += curr_sum
        return ans