# 0795 - K-th Symbol in Grammar
# Date: 2023-10-25
# Runtime: 44 ms, Memory: 16.2 MB
# Submission Id: 1083656209


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return (k-1).bit_count() & 1