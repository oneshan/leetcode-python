# 0338 - Counting Bits
# Date: 2022-10-15
# Runtime: 91 ms, Memory: 20.7 MB
# Submission Id: 822761572


class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = [0] * (n+1)
        b_range = 1
        while b_range <= n:
            start = 0
            for i in range(min(b_range, n-b_range+1)):
                ans[b_range+i] = ans[i] + 1
            b_range <<= 1
            
        return ans