# 2571 - Find the Pivot Integer
# Date: 2022-11-27
# Runtime: 51 ms, Memory: 13.9 MB
# Submission Id: 850690315


from math import isqrt
class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n+1) // 2
        x = isqrt(total)
        return x if x ** 2 == total else -1