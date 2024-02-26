# 0070 - Climbing Stairs
# Date: 2022-05-03
# Runtime: 64 ms, Memory: 13.8 MB
# Submission Id: 692383022


class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1
        for i in range(n-1):
            one, two = two, one + two
        return two