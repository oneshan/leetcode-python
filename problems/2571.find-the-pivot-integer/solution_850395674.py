# 2571 - Find the Pivot Integer
# Date: 2022-11-27
# Runtime: 127 ms, Memory: 13.9 MB
# Submission Id: 850395674


class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (n+1) * n // 2
        curr = 0
        for i in range(1, n+1):
            curr += i
            if curr == total - curr+i:
                return i
        return -1