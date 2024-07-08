# 0060 - Permutation Sequence
# Date: 2024-06-07
# Runtime: 37 ms, Memory: 16.6 MB
# Submission Id: 1279768412


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.ans = []

        @cache
        def factor(n):
            res = 1
            for i in range(1, n+1):
                res *= i
            return res

        def recur(idx, k, mask):
            if idx == 0:
                return

            perm = factor(idx-1)
            for i in range(n):
                if mask & (1 << i):
                    continue
                if perm >= k:
                    self.ans.append(str(i+1))
                    return recur(idx-1, k, mask | (1 << i))
                k -= perm

        recur(n, k, 0)
        return ''.join(self.ans)