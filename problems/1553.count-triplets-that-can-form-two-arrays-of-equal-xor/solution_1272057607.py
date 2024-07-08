# 1553 - Count Triplets That Can Form Two Arrays of Equal XOR
# Date: 2024-05-30
# Runtime: 52 ms, Memory: 16.5 MB
# Submission Id: 1272057607


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # a = b -> a^b = 0
        # prefix[k+1] - prefix[i] = 0 --> (i, k)
        prefix = [0] * (1 + len(arr))
        for i in range(len(arr)):
            prefix[i+1] = prefix[i] ^ arr[i]

        n = len(prefix)
        ans = 0
        for i in range(n):
            for k in range(i+1, n):
                if prefix[i] == prefix[k]:
                    ans += k - i - 1
        return ans