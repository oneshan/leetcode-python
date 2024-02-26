# 1141 - How Many Apples Can You Put into the Basket
# Date: 2023-09-17
# Runtime: 99 ms, Memory: 16.3 MB
# Submission Id: 1051647006


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        
        ans = total = 0
        for w in weight:
            total += w
            if total > 5000:
                break
            ans += 1
        return ans