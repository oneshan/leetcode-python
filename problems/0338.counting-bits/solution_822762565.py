# 0338 - Counting Bits
# Date: 2022-10-15
# Runtime: 96 ms, Memory: 20.9 MB
# Submission Id: 822762565


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1, n+1):
            ans[i] = ans[i&(i-1)] + 1
        return ans