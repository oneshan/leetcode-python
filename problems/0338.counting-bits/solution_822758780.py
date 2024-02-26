# 0338 - Counting Bits
# Date: 2022-10-15
# Runtime: 445 ms, Memory: 20.8 MB
# Submission Id: 822758780


class Solution:
    def countBits(self, n: int) -> List[int]:
        def one_bits(num):
            count = 0
            while num:
                num &= num-1
                count += 1
            return count
        
        ans = [0] * (n+1)
        for i in range(n+1):
            ans[i] = one_bits(i)
        return ans