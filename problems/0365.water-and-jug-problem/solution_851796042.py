# 0365 - Water and Jug Problem
# Date: 2022-11-29
# Runtime: 52 ms, Memory: 13.9 MB
# Submission Id: 851796042


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0