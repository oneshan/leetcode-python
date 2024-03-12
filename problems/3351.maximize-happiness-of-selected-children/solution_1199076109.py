# 3351 - Maximize Happiness of Selected Children
# Date: 2024-03-10
# Runtime: 763 ms, Memory: 43.7 MB
# Submission Id: 1199076109


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        
        ans = 0
        for i in range(k):
            num = happiness[i] - i
            if num < 0:
                break
            ans += num
        return ans