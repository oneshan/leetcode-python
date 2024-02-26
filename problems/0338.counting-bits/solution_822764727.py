# 0338 - Counting Bits
# Date: 2022-10-15
# Runtime: 210 ms, Memory: 20.8 MB
# Submission Id: 822764727


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1, n+1):
            ans[i] = ans[i>>1] + (i&1)
        return ans