# 1553 - Count Triplets That Can Form Two Arrays of Equal XOR
# Date: 2024-06-02
# Runtime: 127 ms, Memory: 16.5 MB
# Submission Id: 1275401994


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for j in range(1, n):
            i, k = j-1, j
            a = b = 0
            counter = Counter()
            while i >= 0:
                a ^= arr[i]
                counter[a] += 1
                i -= 1
            while k < n:
                b ^= arr[k]
                ans += counter[b]
                k += 1

        return ans