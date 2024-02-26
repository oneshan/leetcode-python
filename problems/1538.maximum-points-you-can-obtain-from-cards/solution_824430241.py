# 1538 - Maximum Points You Can Obtain from Cards
# Date: 2022-10-17
# Runtime: 1139 ms, Memory: 27.3 MB
# Submission Id: 824430241


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = 0
        for i in range(k):
            total += cardPoints[i]
         
        ans = total
        for i in range(1, k+1):
            total += cardPoints[-i] - cardPoints[k-i]
            ans = max(ans, total)
        return ans