# 0338 - Counting Bits
# Date: 2024-05-05
# Runtime: 59 ms, Memory: 23.2 MB
# Submission Id: 1249977303


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1, n+1):
            ans[i] = ans[i>>1] + (i & 1)
        return ans