# 0795 - K-th Symbol in Grammar
# Date: 2022-10-28
# Runtime: 26 ms, Memory: 13.8 MB
# Submission Id: 831514713


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (1 - k&1) ^ self.kthGrammar(n-1, (k+1)>>1)