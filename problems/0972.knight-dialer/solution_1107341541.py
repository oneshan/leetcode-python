# 0972 - Knight Dialer
# Date: 2023-11-27
# Runtime: 216 ms, Memory: 16.4 MB
# Submission Id: 1107341541


class Solution:
    def knightDialer(self, n: int) -> int:
        
        def multiply(A, B):
            res = [[0] * len(B[0]) for _ in range(len(A))]
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD  
            return res
        
        matrix = [
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
        ]
        
        v = [[1] * 10]
        MOD = 1_000_000_007
        n -= 1
        while n:
            if n & 1:
                v = multiply(v, matrix)
            matrix = multiply(matrix, matrix)
            n >>= 1

        return sum(v[0]) % MOD