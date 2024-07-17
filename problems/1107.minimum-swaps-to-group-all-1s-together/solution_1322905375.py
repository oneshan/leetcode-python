# 1107 - Minimum Swaps to Group All 1's Together
# Date: 2024-07-16
# Runtime: 551 ms, Memory: 19.6 MB
# Submission Id: 1322905375


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)

        count = 0
        for i in range(ones):
            count += not data[i]

        ans = count
        for i in range(ones, len(data)):
            count -= not data[i-ones]
            count += not data[i]
            ans = min(ans, count)
        return ans            