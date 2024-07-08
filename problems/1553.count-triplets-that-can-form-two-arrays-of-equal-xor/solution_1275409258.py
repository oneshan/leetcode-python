# 1553 - Count Triplets That Can Form Two Arrays of Equal XOR
# Date: 2024-06-02
# Runtime: 31 ms, Memory: 16.6 MB
# Submission Id: 1275409258


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        counter_cnt = Counter()
        counter_cnt[0] = 1
        counter_idx_sum = Counter()

        curr = 0
        for i in range(n):
            curr ^= arr[i]
            ans += i * (counter_cnt[curr]) - counter_idx_sum[curr]
            counter_cnt[curr] += 1
            counter_idx_sum[curr] += i + 1
        
        return ans