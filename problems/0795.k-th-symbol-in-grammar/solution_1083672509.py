# 0795 - K-th Symbol in Grammar
# Date: 2023-10-25
# Runtime: 40 ms, Memory: 16 MB
# Submission Id: 1083672509


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (1 - k&1) ^ self.kthGrammar(n-1, (k+1)>>1)