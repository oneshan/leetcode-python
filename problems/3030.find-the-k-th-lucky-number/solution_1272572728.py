# 3030 - Find The K-th Lucky Number
# Date: 2024-05-31
# Runtime: 58 ms, Memory: 16.6 MB
# Submission Id: 1272572728


class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        k += 1

        ans = []
        while k > 1:
            ans.append('7' if k & 1 else '4')
            k >>= 1
        return ''.join(ans[::-1])