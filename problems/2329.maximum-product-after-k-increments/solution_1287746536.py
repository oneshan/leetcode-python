# 2329 - Maximum Product After K Increments
# Date: 2024-06-14
# Runtime: 1050 ms, Memory: 33.1 MB
# Submission Id: 1287746536


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        counter = Counter(nums)

        i = min(counter)
        while k:
            cnt = min(counter[i], k)
            counter[i+1] += cnt
            counter[i] -= cnt
            k -= cnt
            if k == 0:
                break
            i += 1
        

        ans = 1
        for num, freq in counter.items():
            ans = (ans * num ** freq) % MOD
        return ans