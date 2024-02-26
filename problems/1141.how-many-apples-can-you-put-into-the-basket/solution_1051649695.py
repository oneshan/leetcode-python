# 1141 - How Many Apples Can You Put into the Basket
# Date: 2023-09-17
# Runtime: 106 ms, Memory: 16.5 MB
# Submission Id: 1051649695


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        bucket = [0] * 1001
        for w in weight:
            bucket[w] += 1
            
        ans, remains = 0, 5000
        for w in range(1001):
            if bucket[w] == 0:
                continue
            taken = min(bucket[w], remains // w)
            if taken == 0:
                break
            ans += taken
            remains -= taken * w
        return ans