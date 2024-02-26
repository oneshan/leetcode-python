# 1236 - N-th Tribonacci Number
# Date: 2023-01-30
# Runtime: 34 ms, Memory: 13.8 MB
# Submission Id: 887880434


class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {0: 0, 1: 1, 2: 1}
        def recur(n):
            if n not in cache:
                cache[n] = recur(n-3) + recur(n-2) + recur(n-1)
            return cache[n]
        return recur(n)