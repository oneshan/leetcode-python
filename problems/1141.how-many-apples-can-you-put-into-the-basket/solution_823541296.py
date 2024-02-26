# 1141 - How Many Apples Can You Put into the Basket
# Date: 2022-10-16
# Runtime: 221 ms, Memory: 14.1 MB
# Submission Id: 823541296


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        bucket = [0] * 1001
        for w in weight:
            bucket[w] += 1
        
        ans = total = 0
        for w in range(1001):
            if bucket[w] == 0:
                continue
                
            take = min(bucket[w], (5000-total) // w)
            if take == 0:
                break
            ans += take
            total += take * w
        return ans