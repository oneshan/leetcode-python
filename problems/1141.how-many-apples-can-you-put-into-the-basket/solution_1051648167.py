# 1141 - How Many Apples Can You Put into the Basket
# Date: 2023-09-17
# Runtime: 105 ms, Memory: 16.4 MB
# Submission Id: 1051648167


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        bucket = [0] * 1001
        for w in weight:
            bucket[w] += 1
            
        ans = total = 0
        for w in range(1001):
            if total > 5000:
                break
            for i in range(bucket[w]):
                total += w
                if total > 5000:
                    break
                ans += 1
        return ans