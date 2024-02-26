# 0795 - K-th Symbol in Grammar
# Date: 2022-10-28
# Runtime: 55 ms, Memory: 13.9 MB
# Submission Id: 831525426


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k <= 1 << (n-2):
            return self.kthGrammar(n-1, k)
        return self.kthGrammar(n-1, k-(1<<(n-2))) ^ 1