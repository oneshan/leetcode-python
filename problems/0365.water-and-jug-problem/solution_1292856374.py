# 0365 - Water and Jug Problem
# Date: 2024-06-19
# Runtime: 41 ms, Memory: 16.5 MB
# Submission Id: 1292856374


class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:

        if x + y < target:
            return False

        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x

        return target % gcd(x, y) == 0