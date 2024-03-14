# 2571 - Find the Pivot Integer
# Date: 2024-03-13
# Runtime: 30 ms, Memory: 16.5 MB
# Submission Id: 1202091974


class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        
        temp = n * (n+1) // 2
        res = int(sqrt(temp))
        return res if res * res == temp else -1