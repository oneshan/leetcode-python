# 2645 - Pass the Pillow
# Date: 2024-07-06
# Runtime: 39 ms, Memory: 16.6 MB
# Submission Id: 1311175270


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time % (2 * n - 2)
        if time < n:
            return time + 1
        return n - 1 - (time - n)