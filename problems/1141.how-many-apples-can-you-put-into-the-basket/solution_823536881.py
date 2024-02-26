# 1141 - How Many Apples Can You Put into the Basket
# Date: 2022-10-16
# Runtime: 280 ms, Memory: 14.2 MB
# Submission Id: 823536881


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