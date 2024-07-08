# 1553 - Count Triplets That Can Form Two Arrays of Equal XOR
# Date: 2024-06-02
# Runtime: 50 ms, Memory: 16.7 MB
# Submission Id: 1275403404


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(n):
            prefix = 0
            for k in range(i, n):
                prefix ^= arr[k]
                if prefix == 0:
                    ans += k-i
        return ans